---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 373
---

# Implementation steps

1. Establish ownership over which aspects of the network and protections are defined centrally,
and which your workload teams can maintain.
2. Create environments to test and deploy changes to your network and its protections. For
example, use a Network Testing account and a Network Production account.
3. Determine how you will store and maintain your templates in a version control system. Store
central templates in a repository that is distinct from workload repositories, while workload
templates can be stored in repositories specific to that workload.
4. Create CI/CD pipelines to test and deploy templates. Define tests to check for misconfigurations
and that templates adhere to your company standards.
