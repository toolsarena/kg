---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 395
---

# AWS Well-Architected Framework Framework

a. With an understanding of your organization's data classification scheme, you can establish
accurate processes for automated identification and classification that align with your
company's policies.
2. Perform an initial scan of your environments for automated identification and classification.
a. An initial full scan of your data can help produce a comprehensive understanding of where
sensitive data resides in your environments. When a full scan is not initially required or
is unable to be completed up-front due to cost, evaluate if data sampling techniques are
suitable to achieve your outcomes. For example, Amazon Macie can be configured to perform
a broad automated sensitive data discovery operation across your S3 buckets. This capability
uses sampling techniques to cost-efficiently perform a preliminary analysis of where sensitive
data resides. A deeper analysis of S3 buckets can then be performed using a sensitive data
discovery job. Other data stores can also be exported to S3 to be scanned by Macie.
b. Establish access control defined in SEC07-BP02 for your data storage resources identified
within your scan.
3. Configure ongoing scans of your environments.
a. The automated sensitive data discovery capability of Macie can be used to perform ongoing
scans of your environments. Known S3 buckets that are authorized to store sensitive data can
be excluded using an allow list in Macie.
4. Incorporate identification and classification into your build and test processes.
a. Identify tools that developers can use to scan data for sensitivity while workloads are in
development. Use these tools as part of integration testing to alert when sensitive data is
unexpected and prevent further deployment.
5. Implement a system or runbook to take action when sensitive data is found in unauthorized
locations.
a. Restrict access to data using auto-remediation. For example, you can move this data to an
S3 bucket with restricted access or tag the object if you use attribute-based access control
(ABAC). Additionally, consider masking the data when it is detected.
b. Alert your data protection and incident response teams to investigate the root cause of the
incident. Any learnings they identify can help prevent future incidents.
