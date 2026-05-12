---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 282
---

# Implementation guidance

When following the practices described in SEC01-BP01 Separate workloads using accounts, you
will end up with multiple AWS accounts for different environments that you manage using AWS
Organizations. While each of these environments and workloads may need distinct security
controls, you can standardize some security controls across your organization. Examples include
integrating centralized identity providers, defining networks and firewalls, and configuring
standard locations for storing and analyzing logs. In the same way you can use infrastructure as
code (IaC) to apply the same rigor of application code development to infrastructure provisioning,
you can use IaC to define and deploy your standard security controls as well.
Wherever possible, define your security controls in a declarative way, such as in AWS
CloudFormation, and store them in a source control system. Use DevOps practices to automate
the deploying your controls for more predictable releases, automated testing using tools
like AWS CloudFormation Guard, and detecting drift between your deployed controls and your
desired configuration. You can use services such as AWS CodePipeline, AWS CodeBuild, and
AWS CodeDeploy to construct a CI/CD pipeline. Consider the guidance in Organizing Your AWS
