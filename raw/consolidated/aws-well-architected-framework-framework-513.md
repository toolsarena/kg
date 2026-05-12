---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 666
---

# AWS Well-Architected Framework Framework

• Never experimenting under real-world conditions and expected load.
• Not treating your experiments as code or maintaining them through the development cycle.
• Not running chaos experiments both as part of your CI/CD pipeline, as well as outside of
deployments.
• Neglecting to use past post-incident analyses when determining which faults to experiment with.
Benefits of establishing this best practice: Injecting faults to verify the resilience of your workload
allows you to gain confidence that the recovery procedures of your resilient design will work in the
case of a real fault.
Level of risk exposed if this best practice is not established: Medium
