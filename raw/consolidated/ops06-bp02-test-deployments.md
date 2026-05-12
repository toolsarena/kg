---
title: "OPS06-BP02 Test deployments"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 176
---

# OPS06-BP02 Test deployments

Test release procedures in pre-production by using the same deployment configuration, security
controls, steps, and procedures as in production. Validate that all deployed steps are completed
as expected, such as inspecting files, configurations, and services. Further test all changes with
functional, integration, and load tests, along with any monitoring such as health checks. By doing
these tests, you can identify deployment issues early with an opportunity to plan and mitigate
them prior to production.
You can create temporary parallel environments for testing every change. Automate the
deployment of the test environments using infrastructure as code (IaC) to help reduce amount of
work involved and ensure stability, consistency, and faster feature delivery.
Desired outcome: Your organization adopts a test-driven development culture that includes
testing deployments. This ensures teams are focused on delivering business value rather than
managing releases. Teams are engaged early upon identification of deployment risks to determine
the appropriate course of mitigation.


# OPS06-BP03 Employ safe deployment strategies

Safe production roll-outs control the flow of beneficial changes with an aim to minimize any
perceived impact for customers from those changes. The safety controls provide inspection

# OPS06-BP03 Employ safe deployment strategies

Safe production roll-outs control the flow of beneficial changes with an aim to minimize any
perceived impact for customers from those changes. The safety controls provide inspection