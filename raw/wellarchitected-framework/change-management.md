---
title: "Change management"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 41
---

# Change management

Changes to your workload or its environment must be anticipated and accommodated to achieve
reliable operation of the workload. Changes include those imposed on your workload, such as
spikes in demand, and also those from within, such as feature deployments and security patches.
Using AWS, you can monitor the behavior of a workload and automate the response to KPIs. For
example, your workload can add additional servers as a workload gains more users. You can control
who has permission to make workload changes and audit the history of these changes.
The following questions focus on these considerations for reliability.
REL 6: How do you monitor workload resources?
Logs and metrics are powerful tools to gain insight into the health of your workload. You can
configure your workload to monitor logs and metrics and send notifications when thresholds
are crossed or significant events occur. Monitoring allows your workload to recognize when low-
performance thresholds are crossed or failures occur, so it can recover automatically in response.
REL 7: How do you design your workload to adapt to changes in demand?
A scalable workload provides elasticity to add or remove resources automatically so that they
closely match the current demand at any given point in time.
