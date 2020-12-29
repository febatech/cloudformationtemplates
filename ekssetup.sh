#!/bin/bash
reg="ap-south-1"
nm="EKS-Demo-mumbai-mgd-cluster"
aws eks --region $reg update-kubeconfig --name $nm
aws eks --region $reg describe-cluster --name $nm --query cluster.status
kubectl get svc
