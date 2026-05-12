---
title: "Best practices 36"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 41
---

# Best practices 36

| REL 5: How do you design interactions in a distributed system to mitigate or withstand
failures? |
| --- |
| Distributed systems rely on communications networks to interconnect components (such as
servers or services). Your workload must operate reliably despite data loss or latency over these
networks. Components of the distributed system must operate in a way that does not negatively
impact other components or the workload. These best practices permit workloads to withstand
stresses or failures, more quickly recover from them, and mitigate the impact of such impairmen
ts. The result is improved mean time to recovery (MTTR). |

| REL 6: How do you monitor workload resources? |
| --- |
| Logs and metrics are powerful tools to gain insight into the health of your workload. You can
configure your workload to monitor logs and metrics and send notifications when thresholds
are crossed or significant events occur. Monitoring allows your workload to recognize when low-
performance thresholds are crossed or failures occur, so it can recover automatically in response. |

| REL 7: How do you design your workload to adapt to changes in demand? |
| --- |
| A scalable workload provides elasticity to add or remove resources automatically so that they
closely match the current demand at any given point in time. |
