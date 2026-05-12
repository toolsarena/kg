---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 603
---

# Implementation steps

You can automate deployments to remove manual operations by following these steps:
• Set up a code repository to store your code securely: Use a hosted source code management
system based on a popular technology such as Git to store your source code and infrastructure as
code (IaC) configuration.
• Configure a continuous integration service to compile your source code, run tests, and create
deployment artifacts: To set up a build project for this purpose, see Getting started with AWS
CodeBuild using the console.
• Set up a deployment service that automates application deployments and handles the
complexity of application updates without reliance on error-prone manual deployments:
