---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 394
---

# Implementation guidance

While human judgment is often used to classify data during the initial design phases of a workload,
consider having systems in place that automate identification and classification on test data as a
preventive control. For example, developers can be provided a tool or service to scan representative
data to determine its sensitivity. Within AWS, you can upload data sets into Amazon S3 and scan
them using Amazon Macie, Amazon Comprehend, or Amazon Comprehend Medical. Likewise,
consider scanning data as part of unit and integration testing to detect where sensitive data is
not expected. Alerting on sensitive data at this stage can highlight gaps in protections before
deployment to production. Other features such as sensitive data detection in AWS Glue, Amazon
SNS, and Amazon CloudWatch can also be used to detect PII and take mitigating action. For any
automated tool or service, understand how it defines sensitive data, and augment it with other
human or automated solutions to close any gaps as needed.
As a detective control, use ongoing monitoring of your environments to detect if sensitive data
is being stored in non-compliant ways. This can help detect situations such as sensitive data
being emitted into log files or being copied to a data analytics environment without proper de-
identification or redaction. Data that is stored in Amazon S3 can be continually monitored for
sensitive data using Amazon Macie.
