---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 637
---

# Implementation guidance

AWS services, such as Elastic Load Balancing and Amazon EC2 Auto Scaling, help distribute load
across resources and Availability Zones. Therefore, failure of an individual resource (such as an EC2
instance) or impairment of an Availability Zone can be mitigated by shifting traffic to remaining
healthy resources.
For multi-Region workloads, designs are more complicated. For example, cross-Region read replicas
allow you to deploy your data to multiple AWS Regions. However, failover is still required to
promote the read replica to primary and then point your traffic to the new endpoint. Amazon
Route 53, Amazon Application Recovery Controller (ARC), Amazon CloudFront, and AWS Global
Accelerator can help route traffic across AWS Regions.
AWS services, such as Amazon S3, Lambda, API Gateway, Amazon SQS, Amazon SNS, Amazon SES,
Amazon Pinpoint, Amazon ECR, AWS Certificate Manager, EventBridge, or Amazon DynamoDB, are
