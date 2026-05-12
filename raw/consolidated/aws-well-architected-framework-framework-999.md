---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 330
---

# AWS Well-Architected Framework Framework

can be given access to a broad set of AWS services. We recommend that you evaluate access
continuously and restrict access to only those services and service actions that are necessary to
complete the current job. We recommend this evaluation for both human and machine identities.
Machine identities, sometimes called system or service accounts, are identities that give AWS access
to applications or servers. This access is especially important in a production environment, where
overly permissive permissions can have a broad impact and potentially expose customer data.
AWS provides multiple methods to help identify unused users, roles, permissions, and credentials.
AWS can also help analyze access activity of IAM users and roles, including associated access keys,
and access to AWS resources such as objects in Amazon S3 buckets. AWS Identity and Access
Management Access Analyzer policy generation can assist you in creating restrictive permission
policies based on the actual services and actions a principal interacts with. Attribute-based access
control (ABAC) can help simplify permissions management, as you can provide permissions to users
using their attributes instead of attaching permissions policies directly to each user.
