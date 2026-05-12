---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 594
---

# AWS Well-Architected Framework Framework

• You run automated tests in an environment that does not closely resemble the production
environment.
• You build a test suite that is insufficiently flexible and is difficult to maintain, update, or scale as
the application evolves.
Benefits of establishing this best practice: Automated testing during the deployment process
catches issues early, which reduces the risk of a release to production with bugs or unexpected
behavior. Unit tests validate the code behaves as desired and API contracts are honored.
Integration tests validate that the system operates according to specified requirements. These
types of tests verify the intended working order of components such as user interfaces, APIs,
databases, and source code.
Level of risk exposed if this best practice is not established: High
