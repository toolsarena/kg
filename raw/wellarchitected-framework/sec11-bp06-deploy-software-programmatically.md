---
title: "SEC11-BP06 Deploy software programmatically"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 461
---

# SEC11-BP06 Deploy software programmatically

Perform software deployments programmatically where possible. This approach reduces the
likelihood that a deployment fails or an unexpected issue is introduced due to human error.
Desired outcome: The version of your workload that you test is the version that you deploy,
and the deployment is performed consistently every time. You externalize the configuration
of your workload, which helps you deploy to different environments without changes. You
employ cryptographic signing of your software packages to verify that nothing changes between
environments.
