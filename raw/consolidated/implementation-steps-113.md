---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 565
---

# Implementation steps

1. Choose collection, storage, analysis, and display mechanisms for your observability data.
2. Install and configure metric and log collectors on the appropriate components of your workload
(for example, on Amazon EC2 instances and in sidecar containers). Configure these collectors
to restart automatically if they unexpectedly stop. Enable disk or memory buffering for the
collectors so that temporary publication failures don't impact your applications or result in lost
data.
3. Enable logging on AWS services you use as a part of your workloads, and forward those logs to
the storage service you selected if needed. Refer to the respective services' user or developer
guides for detailed instructions.
4. Define the operational metrics relevant to your workloads that are based on your telemetry
data. These could be based on direct metrics emitted from your workload components, which
can include business KPI related metrics, or the results of aggregated calculations such as sums,
rates, percentiles, or histograms. Calculate these metrics using your log analyzer, and place them
on dashboards as appropriate.
5. Prepare appropriate log queries to analyze workload components, requests, or transaction
behavior as needed.
6. Define and enable a log retention policy for your component logs. Periodically delete logs when
they become older than the policy permits.
