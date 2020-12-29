from __future__ import print_function
from boto3.session import Session

import json
import urllib
import boto3
import zipfile
import tempfile
import botocore
import traceback
import time

print('Loading function')
cf = boto3.client('cloudformation')
s3 = boto3.client('s3')
eks = boto3.client('eks')

##Global Variables
vpcstacknm='myvpcstackforeks'
templateurl='https://myeksfiles.s3.ap-south-1.amazonaws.com/vpc-2public-2private-subnets.yaml'
cvoteamplateurl=''
cvostacknm=''

#1 : Create CVO for K8s Cluster persistent volume storage add the waiting conditions
def create_cvo_stack_forK8S(vpcstacknm, templateurl):
    cf.create_stack(
    StackName=cvostacknm,
    TemplateURL=cvoteamplateurl,
    DisableRollback=False,
    EnableTerminationProtection=False
)
create_cvo_stack_forK8S(cvostacknm,cvoteamplateurl)

#2 : Create VPC for EKS cluster might need to add the waiting conditions
def create_vpc_stack_forEKS(vpcstacknm, templateurl):
    cf.create_stack(
    StackName=stacknm,
    TemplateURL=templateurl,
    DisableRollback=False,
    EnableTerminationProtection=False
)
create_vpc_stack(vpcstacknm,templateurl)

#3: Create the EKS cluster using managed managedcluster.yaml. might need to add the waiting conditions to it
def create_eks_stack():
    subprocess.call(shlex.split('/Users/venkataponnapalli/PycharmProjects/pythonProject/venv/managedcluster.sh'))

#4: Tun the  ekssetup.sh to have communication with K8S and EKS
def run_eks_sh_script():
    subprocess.call(shlex.split('/Users/venkataponnapalli/PycharmProjects/pythonProject/venv/ekssetup.sh'))

#5: Create SC and PV for the K*S deployment
def run_k8s_sh_script():
    subprocess.call(shlex.split('/Users/venkataponnapalli/PycharmProjects/pythonProject/venv/netapp-nfs-sc.sh'))
    subprocess.call(shlex.split('/Users/venkataponnapalli/PycharmProjects/pythonProject/venv/netapp-nfs-pv.sh'))

#6: Create Deployment for WEB APP
def run_k8s_sh_script_fordeploy():
    subprocess.call(shlex.split('/Users/venkataponnapalli/PycharmProjects/pythonProject/venv/myweb-deployment-nfs-netapp-pv.sh'))
