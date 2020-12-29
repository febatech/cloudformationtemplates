#!/usr/bin/env python

###############################
import json
import logging
import shlex
import subprocess
import sys
import time
import boto3
from Naked.toolshed.shell import execute_rb
# AWS Region
from botocore.exceptions import ClientError

############################################################################
# Config you might want to change
############################################################################

region = "ap-south-1"

#VPC stack Variables
VPCStackOuput ={ }

# K8s version to deploy
k8s_version = "1.18"

# Worker instance types to deploy
instance_type = "t2.medium"

############################################################################
# Config you might not want to change
############################################################################

# Names for VPC ,Netapp and worker stack
vpc_stack =  'myMumbaiVPC'
netapp_stack='netapp-ontap-stack'

# CloudFormation templates for VPC and worker nodes
vpc_template = "https://myeksfiles.s3.ap-south-1.amazonaws.com/Vpc-2public-2private-AZs.yaml"
netapp_template='https://febatech-project-pocs.s3.ap-south-1.amazonaws.com/netapp-cvo-sunjay/quickstart-netapp-ontapcloud-sql/templates/netapp-otc-master.yaml'

# K8s IAM role name to use
k8s_admin_role_name = "MyEksadminRole"

# Config file to write kubectl configuration to.
config_file = "kubeconfig.yaml"

# Keypair for accessing workers.  Keypair name and filename.
keypair_name = "kd"
secret_file = "secret.pem"

# Image names for AMIs providing workers.
node_images = {
    "ap-south-1": "ami-08f63db601b82ff5f",
    "us-east-1": "ami-04d29b6f966df1537"
}

# Filename to write internal auth thing to.
worker_auth = "aws-auth-cm.yaml"

############################################################################
# Connect AWS
############################################################################

# Connect to AWS, EC2, cloudformation, IAM and EKS
s = boto3.Session(region_name=region)
ec2 = s.client("ec2")
cf = s.client("cloudformation")
iam = s.client("iam")
eks = s.client("eks")

############################################################################
# IAM role for K8s
############################################################################

print("*** IAM role")

try:

    # See if role exists.
    role = iam.get_role(RoleName=k8s_admin_role_name)
    print("IAM role exists." , role)

except:

    print("IAM role does not exist.  Creating...")

    # This is an AWS role policy document.  Allows access for EKS.
    policy_doc = json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "sts:AssumeRole",
                "Effect": "Allow",
                "Principal": {
                    "Service": "eks.amazonaws.com"
                }
            }
        ]
    })

    # Create role.
    iam.create_role(
        RoleName=k8s_admin_role_name,
        AssumeRolePolicyDocument=policy_doc,
        Description="Role providing access to EKS resources from EKS"
    )

    print( "Role created.")
    print( "Attaching policies...")

    # Add policies allowing access to EKS API.

    iam.attach_role_policy(
        RoleName=k8s_admin_role_name,
        PolicyArn="arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
    )

    iam.attach_role_policy(
        RoleName=k8s_admin_role_name,
        PolicyArn="arn:aws:iam::aws:policy/AmazonEKSServicePolicy"
    )

    print("Attached.")

# Get role ARN for later.
role = iam.get_role(RoleName=k8s_admin_role_name)
role_arn = role["Role"]["Arn"]


############################################################################
# VPC stack
############################################################################

# The VPC stack is a VPC and subnetworks to allow K8s communication.

# Check if a stack exists.
def stack_exists(cf, name):
    try:
        stack = cf.describe_stacks(StackName=name)
        return True
    except:
        return False

print("*** VPC stack")
if stack_exists(cf, vpc_stack):
    # If stack exists, do nothing.
    print("VPC stack already exists")

else:

    print("Creating VPC stack...")

    # Create VPC stack.
    response = cf.create_stack(
        StackName=vpc_stack,
        TemplateURL=vpc_template,
        Parameters=[],
        TimeoutInMinutes=15,
        OnFailure='DELETE'
    )

    if response == None:
        print("Could not create VPC stack")
        sys.exit(1)

    if not "StackId" in response:
        print("Could not create VPC stack")
        sys.exit(1)

    # Get stack ID for later.
    stack_id = response["StackId"]

    print("Created stack " + vpc_stack)
    print("Waiting for VPC stack creation to complete...")

    try:

        # A waiter is something which polls AWS to find out if an operation
        # has completed.
        waiter = cf.get_waiter('stack_create_complete')

        # Wait for stack creation to complet
        res = waiter.wait(
            StackName=vpc_stack,
        )

    except:

        # If waiter fails, that'll be the thing taking too long to deploy.
        print("Gave up waiting for stack to create")
        sys.exit(1)

    print("Stack created")

# Get output information from the stack: VPC ID, security group and subnet IDs.
stack = cf.describe_stacks(StackName=vpc_stack)
vpc_sg = None
vpc_subnet_ids = None
vpc_id = None

# Loop over outputs grabbing information.
for v in stack["Stacks"][0]["Outputs"]:
    if v["OutputKey"] == "SecurityGroups":
        vpc_sg = v["OutputValue"]
    if v["OutputKey"] == "VpcId":
        vpc_id = v["OutputValue"]
    VPCStackOuput['vpc_id'] = vpc_id
    if v["OutputKey"] == "SubnetIds":
        vpc_subnet_ids = v["OutputValue"]
    if v["OutputKey"] == "PublicSubnetIds":
        vpc_public_subnet_ids = v["OutputValue"]
        VPCStackOuput ['vpc_public_subnet_ids'] = vpc_public_subnet_ids
    if v["OutputKey"] == "PrivateSubnetIds":
        vpc_private_subnet_ids = v["OutputValue"]

print("VPC ID: %s" % vpc_id)
print("VPC security group: %s" % vpc_sg)
print("VPC All subnet IDs: %s" % vpc_subnet_ids)
print("VPC Public subnet IDs: %s" % vpc_public_subnet_ids)
print("VPC Private subnet IDs: %s" % vpc_private_subnet_ids)

# Split subnet IDs - it's comma separated.
vpc_subnet_ids = vpc_subnet_ids.split(",")
vpc_public_subnet_ids = vpc_public_subnet_ids.split(",")

VPCStackOuput['pubsubnet1_a'] =  vpc_subnet_ids[0]
VPCStackOuput['pubsubnet1_b'] =  vpc_subnet_ids[1]
VPCStackOuput['prisubnet1_a'] =  vpc_subnet_ids[2]
VPCStackOuput['prisubnet1_b'] =  vpc_subnet_ids[3]
############################################################################
# Netapp Stack
############################################################################

def stack_exists(cf, netapp_stack):
    try:
        stack = cf.describe_stacks(StackName=netapp_stack)
        return True
    except:
        return False

print("*** Netapp stack")

if stack_exists(cf, netapp_stack):
    # If stack exists, do nothing.
    print("Netapp stack already exists")

else:
    print("Creating Netapp stack...")
    # Create Netapp stack.
    response = cf.create_stack(
        StackName=netapp_stack,
        Capabilities=["CAPABILITY_IAM","CAPABILITY_AUTO_EXPAND","CAPABILITY_NAMED_IAM"],
        TemplateURL=netapp_template,
        Parameters=[
        {
        'ParameterKey': 'CloudManagerPassword',
            'ParameterValue': 'FebaTech$123'
        },
        {
        'ParameterKey': 'CloudManagerUserEmail',

            'ParameterValue': 'awspearls@febatech.com'
        },
        {
        'ParameterKey': 'CompanyName',

            'ParameterValue': 'FebaTech'
        },
        {
        'ParameterKey': 'KeyPair',

            'ParameterValue': 'guru'
        },
        {
        'ParameterKey': 'QSS3BucketName',

            'ParameterValue': 'febatech-project-pocs'
        },
        {
        'ParameterKey': 'QSS3KeyPrefix',

            'ParameterValue': 'netapp-cvo-sunjay/quickstart-netapp-ontapcloud-sql'
        },
        {
        'ParameterKey': 'RemoteAccessCIDR',

            'ParameterValue': '0.0.0.0/0'
        },
       {
                'ParameterKey': 'VPCCIDR',
                'ParameterValue': '172.18.0.0'
        },
        {
        'ParameterKey': 'VPCId',

            'ParameterValue': vpc_id
        },
        {
        'ParameterKey': 'SubnetId',

            'ParameterValue': vpc_public_subnet_ids[0]
        },

        ],
        TimeoutInMinutes=45,
        OnFailure='DELETE'
    )

    if response == None:
        print("Could not create Netapp stack")
        sys.exit(1)

    if not "StackId" in response:
        print("Could not create Netapp stack")
        sys.exit(1)

    # Get stack ID for later.
    stack_id = response["StackId"]

    print("Created stack " + stack_id)
    print("Waiting for Netapp stack creation to complete...")

    try:

        # A waiter is something which polls AWS to find out if an operation
        # has completed.
        waiter = cf.get_waiter('stack_create_complete')

        # Wait for stack creation to complet
        res = waiter.wait(
            StackName=netapp_stack,
        )
    except:
       # If waiter fails, that'll be the thing taking too long to deploy.
        print("Gave up waiting for stack to create")
        sys.exit(1)

    print("Stack created")

netappstack = cf.describe_stacks(StackName=netapp_stack)
    # Loop over outputs grabbing information.
for netapp in netappstack["Stacks"][0]["Outputs"]:
    if netapp["OutputKey"] == "CloudManagerURL":
            netapp_url = netapp["OutputValue"]
    if netapp["OutputKey"] == "CVOMountPoint":
            CVOMountPt = netapp["OutputValue"]

print("netapp URL is : %s" % netapp_url)
print("CVO Mount point is: %s" % CVOMountPt)

################DONE#################################################################

file = open("VPCNetAppOutput.txt", "w")
str_dictionary = VPCStackOuput
file.write(str_dictionary["vpc_id"])
file.write("\n")
file.write(str_dictionary["pubsubnet1_a"])
file.write("\n")
file.write(str_dictionary["pubsubnet1_b"])
file.write("\n")
file.write(str_dictionary["prisubnet1_a"])
file.write("\n")
file.write(str_dictionary["prisubnet1_b"])
file.write("\n")
file.close()
############ Create EKS cluster ##################################################
clustercount=1
try:
 if clustercount == 0:
    success = execute_rb('read_config.rb')
    time.sleep(5)
    if success:
        print("managedcluster.yaml is generated")
        subprocess.call(shlex.split(
            '/Users/venkataponnapalli/PycharmProjects/pythonProject/docker-images-for-k8s-eks-deployments/managedcluster.sh'))
        time.sleep(1800)
        print(" Cluster is created")
    else:
        sys.exit()
    clustercount += 1
except ClientError as e:
        logging.error(e)
print( "EKS Cluster created")
############ Setup the EKSSETUP ##################################################
setupcount=1
try:
    if setupcount==0:
        print("execute eks setup ")
        subprocess.call(shlex.split(
        '/Users/venkataponnapalli/PycharmProjects/pythonProject/docker-images-for-k8s-eks-deployments/ekssetup.sh'))
        time.sleep(10)
    else:
        print ( 'Already setup is done')
except ClientError as e:
        logging.error(e)
print(" Execute Cluster setup done and active now")
############Setup the NFS Storage Class  ##################################################
storagecount=1
try:
    if storagecount==0:
        print("execute storage class setup")
        subprocess.call(shlex.split(
        '/Users/venkataponnapalli/PycharmProjects/pythonProject/docker-images-for-k8s-eks-deployments/netapp-nfs-sc.sh'))
        time.sleep(10)
    else:
        print ( 'Already SC is created')

except ClientError as e:
        logging.error(e)
print(" storage class is created and active now")
############Setup the NSF PV  ##################################################
pvcount=1
try:
    if pvcount==0:
        print("execute PV setup")
        subprocess.call(shlex.split(
        '/Users/venkataponnapalli/PycharmProjects/pythonProject/docker-images-for-k8s-eks-deployments/netapp-nfs-pv.sh'))
        time.sleep(12)
    else:
        print('Already PV is created')

except ClientError as e:
        logging.error(e)
print(" PV is created and active now")

############Finally WEB Deployment  ##################################################
wedepcount=0
try:
    if wedepcount==0:
        print("execute WEB Deployment setup")
        subprocess.call(shlex.split(
        '/Users/venkataponnapalli/PycharmProjects/pythonProject/docker-images-for-k8s-eks-deployments/myweb-deployment-nfs-netapp-pv.sh'))
        time.sleep(20)
    else:
        print('Already WEB Deplmnt is created')

except ClientError as e:
        logging.error(e)
print(" WEB Deplmnt is created and active now")
