---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 365
---

# Implementation steps

1. Review your workload architecture. Logically group components and services based on the
functions they serve, the sensitivity of data being processed, and their behavior.
2. For components responding to requests from the internet, consider using load balancers or
other proxies to provide public endpoints. Explore shifting security controls by using managed
services, such as CloudFront, Amazon API Gateway, Elastic Load Balancing, and AWS Amplify to
host public endpoints.
3. For components running in compute environments, such as Amazon EC2 instances, AWS Fargate
containers, or Lambda functions, deploy these into private subnets based on your groups from
the first step.
4. For fully managed AWS services, such as Amazon DynamoDB, Amazon Kinesis, or Amazon SQS,
consider using VPC endpoints as the default for access over private IP addresses.
