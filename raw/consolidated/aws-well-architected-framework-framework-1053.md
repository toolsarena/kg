---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 397
---

# AWS Well-Architected Framework Framework

• Relying on data durability as a substitute for data backups and protection.
• Retaining data beyond its usefulness and required retention period.
Benefits of establishing this best practice: A well-defined and scalable data lifecycle management
strategy helps maintain regulatory compliance, improves data security, optimizes storage costs,
and enables efficient data access and sharing while maintaining appropriate controls.
Level of risk exposed if this best practice is not established: High


# AWS Well-Architected Framework Framework

SEC 8. How do you protect your data at rest?
Protect your data at rest by implementing multiple controls, to reduce the risk of unauthorized
access or mishandling.

# AWS Well-Architected Framework Framework

a. Some organizations prefer to segregate the AWS KMS logging activity into a separate trail.
For more detail, see the Logging AWS KMS API calls with CloudTrail section of the AWS KMS
developers guide.

# AWS Well-Architected Framework Framework

of protection against unintended data disclosure or exfiltration. You maintain an inventory of
unencrypted data and understand the controls that are in place to protect it.