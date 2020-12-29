#!/bin/bash
cnm="EKS-Demo-mumbai-mgd-cluster"
ngprivate="EKS-managed-private-workers"
ngpublic="EKS-managed-public-workers"
desired=2
min=2
max=2
eksctl scale nodegroup --cluster=$cnm --name=$ngprivate --nodes=$desired --nodes-min=$min --nodes-max=$max
eksctl scale nodegroup --cluster=$cnm --name=$ngpublic --nodes=$desired --nodes-min=$min --nodes-max=$max


