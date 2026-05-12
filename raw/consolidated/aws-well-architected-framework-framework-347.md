---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 462
---

# AWS Well-Architected Framework Framework

deployments. You can use these services to automate the build, test, and deployment processes,
which reduces manual intervention and increases consistency.
To further enhance security and traceability, you can sign your application packages after they
have been tested and validate these signatures during deployment. To do so, use cryptographic
tools such as AWS Signer or AWS Key Management Service (AWS KMS). By signing and verifying
packages, you can make sure that you deploy only authorized and validated code to your
environments.
Additionally, your team can architect your workload to obtain environment-specific configuration
data from an external source, such as AWS Systems Manager Parameter Store. This practice
separates the application code from the configuration data, which helps you manage and update
configurations independently without modifying the application code itself.


# AWS Well-Architected Framework Framework

• Configure the pipeline to automatically build, test, and deploy your application code to the
respective environments.
• Integrate code repositories with the CI/CD pipeline for version control and code management.

# AWS Well-Architected Framework Framework

• Implement auditing and compliance checks to verify adherence to security best practices and
regulatory requirements.