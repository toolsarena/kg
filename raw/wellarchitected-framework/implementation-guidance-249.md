---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 882
---

# Implementation guidance

Consider the cost of services and options when selecting all components. This includes using
application level and managed services, such as Amazon Relational Database Service (Amazon
RDS), Amazon DynamoDB, Amazon Simple Notification Service (Amazon SNS), and Amazon Simple
Email Service (Amazon SES) to reduce overall organization cost.
Use serverless and containers for compute, such as AWS Lambda and Amazon Simple Storage
Service (Amazon S3) for static websites. Containerize your application if possible and use AWS
Managed Container Services such as Amazon Elastic Container Service (Amazon ECS) or Amazon
Elastic Kubernetes Service (Amazon EKS).
Minimize license costs by using open-source software, or software that does not have license fees
(for example, Amazon Linux for compute workloads or migrate databases to Amazon Aurora).
You can use serverless or application-level services such as Lambda, Amazon Simple Queue Service
(Amazon SQS), Amazon SNS, and Amazon SES. These services remove the need for you to manage
a resource and provide the function of code execution, queuing services, and message delivery. The
other benefit is that they scale in performance and cost in line with usage, allowing efficient cost
allocation and attribution.
Using event-driven architecture is also possible with serverless services. Event-driven architectures
are push-based, so everything happens on demand as the event presents itself in the router.
This way, you’re not paying for continuous polling to check for an event. This means less
network bandwidth consumption, less CPU utilization, less idle fleet capacity, and fewer SSL/TLS
handshakes.
For more information on serverless, see Well-Architected Serverless Application lens whitepaper.
