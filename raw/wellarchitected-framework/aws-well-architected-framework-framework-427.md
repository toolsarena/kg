---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 560
---

# AWS Well-Architected Framework Framework

AWS makes an abundance of monitoring and log information available for consumption that can
be used to define workload-specific metrics, change-in-demand processes, and adopt machine
learning techniques regardless of ML expertise.
In addition, monitor all of your external endpoints to ensure that they are independent of your
base implementation. This active monitoring can be done with synthetic transactions (sometimes
referred to as user canaries, but not to be confused with canary deployments) which periodically
run a number of common tasks matching actions performed by clients of the workload. Keep
these tasks short in duration and be sure not to overload your workload during testing. Amazon
CloudWatch Synthetics allows you to create synthetic canaries to monitor your endpoints and APIs.
You can also combine the synthetic canary client nodes with AWS X-Ray console to pinpoint which
synthetic canaries are experiencing issues with errors, faults, or throttling rates for the selected
time frame.
