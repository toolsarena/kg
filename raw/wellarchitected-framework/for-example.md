---
title: "For example:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 671
---

# For example:

• If 20% of the nodes in the Amazon EKS node-group are taken down, the Transaction Create
API continues to serve the 99th percentile of requests in under 100 ms (steady state).
The Amazon EKS nodes will recover within five minutes, and pods will get scheduled and
process traffic within eight minutes after the initiation of the experiment. Alerts will fire
within three minutes.
• If a single Amazon EC2 instance failure occurs, the order system’s Elastic Load Balancing
health check will cause the Elastic Load Balancing to only send requests to the remaining
healthy instances while the Amazon EC2 Auto Scaling replaces the failed instance,
maintaining a less than 0.01% increase in server-side (5xx) errors (steady state).
• If the primary Amazon RDS database instance fails, the Supply Chain data collection
workload will failover and connect to the standby Amazon RDS database instance to
maintain less than 1 minute of database read or write errors (steady state).
c. Run the experiment by injecting the fault.
An experiment should by default be fail-safe and tolerated by the workload. If you know that
the workload will fail, do not run the experiment. Chaos engineering should be used to find
known-unknowns or unknown-unknowns. Known-unknowns are things you are aware of but
don’t fully understand, and unknown-unknowns are things you are neither aware of nor fully
understand. Experimenting against a workload that you know is broken won’t provide you
with new insights. Your experiment should be carefully planned, have a clear scope of impact,
and provide a rollback mechanism that can be applied in case of unexpected turbulence. If
your due-diligence shows that your workload should survive the experiment, move forward
