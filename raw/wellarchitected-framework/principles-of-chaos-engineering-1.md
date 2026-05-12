---
title: "Principles of Chaos Engineering"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 666
---

# Principles of Chaos Engineering

If a system is able to withstand these disruptions, the chaos experiment should be maintained as
an automated regression test. In this way, chaos experiments should be performed as part of your
systems development lifecycle (SDLC) and as part of your CI/CD pipeline.
To ensure that your workload can survive component failure, inject real world events as part of
your experiments. For example, experiment with the loss of Amazon EC2 instances or failover of
the primary Amazon RDS database instance, and verify that your workload is not impacted (or
