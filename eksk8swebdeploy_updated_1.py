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

from botocore.exceptions import ClientError

import os


############################################################################
# Config you might want to change
############################################################################

region = "ap-south-1"

#VPC stack Variables
VPCStackOuput ={ }

############################################################################
# Config you might not want to change
############################################################################

# Names for VPC ,Netapp and worker stack
vpc_stack =  'myMumbaiVPC'
netapp_stack='netapp-ontap-stack'

# CloudFormation templates for VPC and worker nodes
vpc_template = "https://myeksfiles.s3.ap-south-1.amazonaws.com/Vpc-2public-2private-AZs.yaml"
netapp_template='https://febatech-project-pocs.s3.ap-south-1.amazonaws.com/netapp-cvo-sunjay/quickstart-netapp-ontapcloud-sql/templates/netapp-otc-master.yaml'


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


############## writing vpc_id and subnet_id to netapp_vpcid_pubsubnet_params file #################
with open('netapp_vpcid_pubsubnet_params', 'w') as f:
    f.write(vpc_id)
    f.write("\n")
    f.write(vpc_public_subnet_ids[0])

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
    import netapp_params                                                           # executes hid_val file and then imports it
    print("Creating Netapp stack...")
    # Create Netapp stack.
    response = cf.create_stack(
        StackName=netapp_stack,
        Capabilities=["CAPABILITY_IAM","CAPABILITY_AUTO_EXPAND","CAPABILITY_NAMED_IAM"],
        TemplateURL=netapp_template,
        Parameters=netapp_params.hidden_values,                                    # assigning the variable, value from hid_val file
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

        # Wait for stack creation to complete
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

VPCStackOuput['CVOMountPt'] = CVOMountPt




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
file.write(CVOMountPt['MountPoint'].split(":")[0])
file.write("\n")
file.write(CVOMountPt['MountPoint'].split(":")[1])
file.close()


############ Varibles House Keeping ###############################################
with open('counter.json') as f:
    data=json.load(f)


list_of_all_counters = ["clustercount","setupcount","storagecount", "pvcount", "wedepcount"]   # add variables in this list


# values for if conditions are fetched from this counters_latest_value list
# after every run, values in this list are incremented by one

counters_latest_value = [{"clustercount": None}, {"setupcount": None}, {"storagecount" : None}, {"pvcount" : None}, {"wedepcount": None}]



count=0
for dict_json in data['var']:                                                                               # fetching a dictionary that is dict_json from json file
    counters_latest_value[count][list_of_all_counters[count]] = dict_json[list_of_all_counters[count]]      # value of variable in json file will be assigned to the respective key in the counters_latest_value dictionary
    dict_json[list_of_all_counters[count]] += 1                                                             # value of variable is updated in json file
    count += 1

with open('counter.json', 'w') as f:
    json.dump(data, f, indent=2)


############ Create EKS cluster ##################################################
try:
 if counters_latest_value[0]["clustercount"] == 0:
    success = execute_rb('read_config.rb')
    time.sleep(5)
    if success:
        print("managedcluster.yaml is generated")
        subprocess.call(shlex.split('managedcluster.sh'))
        time.sleep(1800)
        print(" Cluster is created")
    else:
        sys.exit()
except ClientError as e:
        logging.error(e)
print( "EKS Cluster created")
############ Setup the EKSSETUP ##################################################
try:
    if counters_latest_value[1]["setupcount"]==0:
        print("execute eks setup ")
        subprocess.call(shlex.split('ekssetup.sh'))
        time.sleep(10)
    else:
        print ( 'Already setup is done')
except ClientError as e:
        logging.error(e)
print(" Execute Cluster setup done and active now")
############Setup the NFS Storage Class  ##################################################
try:
    if counters_latest_value[2]["storagecount"]==0:
        print("execute storage class setup")
        subprocess.call(shlex.split('netapp-nfs-sc.sh'))
        time.sleep(10)
    else:
        print ( 'Already SC is created')

except ClientError as e:
        logging.error(e)
print(" storage class is created and active now")



############Setup the NSF PV  ##################################################
try:
    if counters_latest_value[3]["pvcount"]==0:
        print("execute PV setup")
        subprocess.call(shlex.split('netapp-nfs-pv.sh'))
        time.sleep(12)
    else:
        print('Already PV is created')

except ClientError as e:
        logging.error(e)
print(" PV is created and active now")

############Finally WEB Deployment  ##################################################
try:
    if counters_latest_value[4]["wedepcount"]==0:
        print("execute WEB Deployment setup")
        subprocess.call(shlex.split('myweb-deployment-nfs-netapp-pv.sh'))
        time.sleep(20)
    else:
        print('Already WEB Deplmnt is created')

except ClientError as e:
        logging.error(e)
print(" WEB Deplmnt is created and active now")
