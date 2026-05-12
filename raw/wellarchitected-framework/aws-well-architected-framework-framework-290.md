---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 382
---

# AWS Well-Architected Framework Framework

2. Verify that the IAM Roles associated with your EC2 instance profiles include
the AmazonSSMManagedInstanceCore managed IAM policy.
3. Disable SSH, RDP, and other remote access services running on your instances. You can do this
by running scripts configured in the user data section of your launch templates or by building
customized AMIs with tools such as EC2 Image Builder.
4. Verify that the security group ingress rules applicable to your EC2 instances do not permit
access on port 22/tcp (SSH) or port 3389/tcp (RDP). Implement detection and alerting on
misconfigured security groups using services such as AWS Config.
5. Define appropriate automations, runbooks, and run commands in Systems Manager. Use IAM
policies to define who can perform these actions and the conditions under which they are
permitted. Test these automations thoroughly in a non-production environment. Invoke these
automations when necessary, instead of interactively accessing the instance.
6. Use AWS Systems Manager Session Manager to provide interactive access to instances when
necessary. Turn on session activity logging to maintain an audit trail in Amazon CloudWatch
Logs or Amazon S3.
