## Prerequisities 
Before starting you need the following:
* An AWS account
* AWS CLI
* KUBECTL 
* EKSCTL
* Ruby

## Provision EKS cluster with Node group.
* Create cloudformation stack for EKS and Its Node group.
* Create VPC using AWS cloudformation: vpc-2public-2private-subnets.yaml  
* Create an EKS cluster using EKSCTL using this file managedcluster.yaml
* Run this setup script  ekssetup.sh after EKS cluster is created.

## Build StorageClass and PersistentVolume for NetApp Cloud Volume ONTAP to be consumed by K8S Cluster.
* Files to execute in sequence.
*  netapp-nfs-sc.yaml and then netapp-nfs-pv.yaml

## Build deployment file in yaml for all Docker/ECR Images.
* myweb-deployment-nfs-netapp-pv.yaml 
   
## Use kubectl to create deployment or apply deployment to run changes.
* kubectl create -f myweb-deployment-nfs-netapp-pv.yaml 
* kubectl create -f myweb-deployment-nfs-netapp-pv.yaml 
* kubectl apply  -f myweb-deployment-nfs-netapp-pv.yaml  ( updates)
* kubectl apply  -f myweb-deployment-nfs-netapp-pv.yaml  ( updates)

## Finally Run K8S Applications.
  
# Git Repo:
* https://github.com/febatech/docker-images-for-k8s-eks-deployments
* https://eksctl.io/usage/creating-and-managing-clusters/

## To have bash to run in PODS use the following commands.
* kubectl exec -it PODID /bin/bash
* Bash To create a 2 MB file dd if=/dev/urandom of=ostechnix.txt bs=2MB count=1
