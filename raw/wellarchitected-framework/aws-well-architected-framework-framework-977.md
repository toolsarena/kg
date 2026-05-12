---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 300
---

# AWS Well-Architected Framework Framework

Some long-lived secrets might not be able to be removed or replaced. These secrets can be stored
in a service such as AWS Secrets Manager, where they can be centrally stored, managed, and
rotated on a regular basis.
An audit of the workload's source code and configuration files can reveal many types of credentials.
The following table summarizes strategies for handling common types of credentials:
