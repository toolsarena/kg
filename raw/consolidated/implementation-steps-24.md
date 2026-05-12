---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 180
---

# Implementation steps

1. Use an approval workflow to initiate the sequence of production roll-out steps upon promotion
to production .
2. Use an automated deployment system such as AWS CodeDeploy. AWS CodeDeploy deployment
options include in-place deployments for EC2/On-Premises and blue/green deployments for
EC2/On-Premises, AWS Lambda, and Amazon ECS (see the preceding workflow diagram).
a. Where applicable, integrate AWS CodeDeploy with other AWS services or integrate AWS
CodeDeploy with partner product and services.
3. Use blue/green deployments for databases such as Amazon Aurora and Amazon RDS.
4. Monitor deployments using Amazon CloudWatch, AWS CloudTrail, and Amazon Simple
Notification Service (Amazon SNS) event notifications.
