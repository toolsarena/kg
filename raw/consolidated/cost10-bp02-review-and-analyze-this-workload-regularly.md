---
title: "COST10-BP02 Review and analyze this workload regularly"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 928
---

# COST10-BP02 Review and analyze this workload regularly

Existing workloads are regularly reviewed based on each defined process to find out if new services
can be adopted, existing services can be replaced, or workloads can be re-architected.
Level of risk exposed if this best practice is not established: Medium


# COST11-BP01 Perform automation for operations

Evaluate the operational costs on the cloud, focusing on quantifying the time and effort savings
in administrative tasks, deployments, mitigating the risk of human errors, compliance, and other

# COST11-BP01 Perform automation for operations

Evaluate the operational costs on the cloud, focusing on quantifying the time and effort savings
in administrative tasks, deployments, mitigating the risk of human errors, compliance, and other

# Credential type Description Suggested strategy

Application and database Passwords – plain text string Rotate: Store credentials in
credentials AWS Secrets Manager and
establish automated rotation
if possible.
Amazon RDS and Aurora Passwords – plain text string Replace: Use the Secrets

# Credential type Description Suggested strategy

IAM access keys AWS IAM access and secret Replace: Use IAM roles
keys used to assume IAM assigned to the compute
roles inside of a workload instances (such as Amazon
EC2 or AWS Lambda) instead.

# Credential type Description Suggested strategy

Application and database Passwords – plain text string Rotate: Store credentials in
credentials AWS Secrets Manager and
establish automated rotation
if possible.
Amazon RDS and Aurora Passwords – plain text string Replace: Use the Secrets

# Credential type Description Suggested strategy

IAM access keys AWS IAM access and secret Replace: Use IAM roles
keys used to assume IAM assigned to the compute
roles inside of a workload instances (such as Amazon
EC2 or AWS Lambda) instead.

# Custom Resources

• Securely Using External ID for Accessing AWS Accounts Owned by Others
• Extend IAM roles to workloads outside of IAM with IAM Roles Anywhere

# Custom Resources

• Securely Using External ID for Accessing AWS Accounts Owned by Others
• Extend IAM roles to workloads outside of IAM with IAM Roles Anywhere