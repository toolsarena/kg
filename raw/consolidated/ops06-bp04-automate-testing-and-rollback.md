---
title: "OPS06-BP04 Automate testing and rollback"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 182
---

# OPS06-BP04 Automate testing and rollback

To increase the speed, reliability, and confidence of your deployment process, have a strategy
for automated testing and rollback capabilities in pre-production and production environments.
Automate testing when deploying to production to simulate human and system interactions
that verify the changes being deployed. Automate rollback to revert back to a previous known
good state quickly. The rollback should be initiated automatically on pre-defined conditions such
as when the desired outcome of your change is not achieved or when the automated test fails.
Automating these two activities improves your success rate for your deployments, minimizes
recovery time, and reduces the potential impact to the business.
Desired outcome: Your automated tests and rollback strategies are integrated into your
continuous integration, continuous delivery (CI/CD) pipeline. Your monitoring is able to validate
against your success criteria and initiate automatic rollback upon failure. This minimizes any
impact to end users and customers. For example, when all testing outcomes have been satisfied,
you promote your code into the production environment where automated regression testing is
initiated, leveraging the same test cases. If regression test results do not match expectations, then
automated rollback is initiated in the pipeline workflow.
