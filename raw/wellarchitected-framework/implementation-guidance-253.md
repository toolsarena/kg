---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 890
---

# Implementation guidance

Create a feedback loop within the workload that uses active metrics from the running workload to
make changes to that workload. You can use a managed service, such as AWS Auto Scaling, which
you configure to perform the right sizing operations for you. AWS also provides APIs, SDKs, and
features that allow resources to be modified with minimal effort. You can program a workload to
stop-and-start an Amazon EC2 instance to allow a change of instance size or instance type. This
provides the benefits of right-sizing while removing almost all the operational cost required to
make the change.
Some AWS services have built in automatic type or size selection, such as Amazon Simple Storage
Service Intelligent-Tiering. Amazon S3 Intelligent-Tiering automatically moves your data between
two access tiers, frequent access and infrequent access, based on your usage patterns.
