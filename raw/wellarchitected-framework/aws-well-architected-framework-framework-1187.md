---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 569
---

# AWS Well-Architected Framework Framework

Amazon SNS is recommended for applications that need high fan out (thousands or millions of
endpoints). A common pattern we see is that customers use Amazon SNS as a target for their rule
to filter the events that they need, and fan out to multiple endpoints.
Messages are unstructured and can be in any format. Amazon SNS supports forwarding messages
to six different types of targets, including Lambda, Amazon SQS, HTTP/S endpoints, SMS, mobile
push, and email. Amazon SNS typical latency is under 30 milliseconds. A wide range of AWS
services send Amazon SNS messages by configuring the service to do so (more than 30, including
Amazon EC2, Amazon S3, and Amazon RDS).
