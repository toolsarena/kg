---
title: "REL04-BP03 Do constant work"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 530
---

# REL04-BP03 Do constant work

Systems can fail when there are large, rapid changes in load. For example, if your workload is doing
a health check that monitors the health of thousands of servers, it should send the same size
payload (a full snapshot of the current state) each time. Whether no servers are failing, or all of
them, the health check system is doing constant work with no large, rapid changes.
For example, if the health check system is monitoring 100,000 servers, the load on it is nominal
under the normally light server failure rate. However, if a major event makes half of those servers
unhealthy, then the health check system would be overwhelmed trying to update notification
systems and communicate state to its clients. So instead the health check system should send
the full snapshot of the current state each time. 100,000 server health states, each represented
by a bit, would only be a 12.5-KB payload. Whether no servers are failing, or all of them are, the
health check system is doing constant work, and large, rapid changes are not a threat to the system
stability. This is actually how Amazon Route 53 handles health checks for endpoints (such as IP
addresses) to determine how end users are routed to them.
Level of risk exposed if this best practice is not established: Low
