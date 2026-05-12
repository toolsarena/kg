---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 466
---

# Implementation steps

• Start with the AWS Deployment Pipelines Reference Architecture.
• Consider using AWS IAM Access Analyzer to programmatically generate least privilege IAM
policies for the pipelines.
• Integrate your pipelines with monitoring and alerting so that you are notified of unexpected or
abnormal activity, for AWS managed services Amazon EventBridge allows you to route data to
targets such as AWS Lambda or Amazon Simple Notification Service (Amazon SNS).
