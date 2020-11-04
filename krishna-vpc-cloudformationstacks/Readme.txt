Create a new vpc and subnets and launch HA Website in the desired AWS Region. 

Resources defined in the Cloudformation template:
* Vpc: 1
* Public Subnets: 2
* Internet Gateway: 1
* Routing Table: 1
* Launch templates: 1
* Autoscaling Group: 1
* Classic Load balancer: 1
* Ec2 Instances: 2

Description:
* With this Cloudformation template we can deploy new vpc with 2 public subnets and internet gateway attached to VPC . With-in this template We are creating  route tables  for subnet association and also we are adding an internet gateway in the routing table for sending traffic from the subnets. In addition we are creating a launch template with ec2 properties and also creating an autoscaling group with the launch template as a source. By default it deploys 2Ec2 instances with httpd pre-installed with user data in 2 subnets. we are also enabling load balancer to balance the traffic for the desired 2 ec2 instances in the autoscaling group. After deploying all the resources, we can access a html page showing the message “WELCOME TO FEBATECH WEB SERVER” with the load balancer dns name. 

Steps for Launching this Cloudformation template:

1) You can get this cloudformation template with the name “vpc.yaml” from this s3 link:    
         s3://febatech-cf-templates-to-deploy-workloads/Krishna-VPC-CloudFormationStacks/
                                                  or
   You can also clone this template from the below Github url:
         https://github.com/febatech/cloudformationtemplates.git
         
2) After cloning the template, jump to aws console and select Cloudformation service there we can upload our template from our localhost or by s3 bucket url. 

3) After uploading the template click on next, you can specify your stack details and parameters like Instancetype, keyname, ssh location and most importantly        VpcCidr range.

4) On the next step you can go with default stack configuration options so click on next.

5) Finally click on “Create Stack” for deploying all the resources in the template and we can also delete all the resources by clicking on “Delete Stack”.
