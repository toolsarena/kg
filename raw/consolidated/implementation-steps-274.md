---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 177
---

# Implementation steps

1. Perform pre-install checks to mirror the pre-production environment to production.
a. Use drift detection to detect when resources have been changed outside of CloudFormation.
b. Use change sets to validate that the intent of a stack update matches the actions that
CloudFormation takes when the change set is initiated.
2. This triggers a manual approval step in AWS CodePipeline to authorize the deployment to the
pre-production environment.
3. Use deployment configurations such as AWS CodeDeploy AppSpec files to define deployment
and validation steps.
4. Where applicable, integrate AWS CodeDeploy with other AWS services or integrate AWS
CodeDeploy with partner product and services.
