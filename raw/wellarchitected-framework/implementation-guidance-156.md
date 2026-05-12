---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 582
---

# Implementation guidance

To set up automation with CI/CD pipelines and infrastructure as code (IaC) for your AWS
architecture, choose a version control system such as Git to store your IaC templates and
configuration. These templates can be written using tools such as AWS CloudFormation. To start,
define your infrastructure components (such as AWS VPCs, Amazon EC2 Auto Scaling Groups, and
Amazon RDS databases) within these templates.
Next, integrate these IaC templates with a CI/CD pipeline to automate the deployment process.
AWS CodePipeline provides a seamless AWS-native solution, or you can use other third-party CI/CD
solutions. Create a pipeline that activates when changes occur to your version control repository.
Configure the pipeline to include stages that lint and validate your IaC templates, deploy the
infrastructure to a staging environment, run automated tests, and finally, deploy to production.
Incorporate approval steps where necessary to maintain control over changes. This automated
pipeline not only speeds up deployment but also facilitates consistency and reliability across
environments.
Configure Auto Scaling of resources such as Amazon EC2 instances, Amazon ECS tasks, and
database replicas in your IaC to provide automatic scale-out and scale-in as needed. This approach
enhances application availability and performance and optimizes cost by dynamically adjusting
