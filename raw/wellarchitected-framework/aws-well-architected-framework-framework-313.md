---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 414
---

# AWS Well-Architected Framework Framework

for each level in the CA hierarchy, making it simpler to discover anomalies in CloudTrail log data
and reducing the scope of access or impact if there is unauthorized access to one of the accounts.
The root CA should reside in its own separate account and should only be used to issue one or
more intermediate CA certificates.
Then, create one or more intermediate CAs in accounts separate from the root CA's account to
issue certificates for end users, devices, or other workloads. Finally, issue certificates from your
root CA to the intermediate CAs, which will in turn issue certificates to your end users or devices.
For more information on planning your CA deployment and designing your CA hierarchy, including
planning for resiliency, cross-region replication, sharing CAs across your organization, and more,
see Planning your AWS Private CA deployment.
