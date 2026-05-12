---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 557
---

# Implementation guidance

• Identify critical components in your workload.
• Design and architect the critical components in your workload to withstand failure of non-critical
components.
• Conduct testing to validate the behavior of your critical components during the failure of non-
critical components.
• Define and monitor relevant metrics or triggers to initiate emergency lever procedures.
• Define the procedures (manual or automated) that comprise the emergency lever.


# Implementation guidance

1. Turn on logging where available. Monitoring data should be obtained from all components of
the workloads. Turn on additional logging, such as S3 Access Logs, and permit your workload