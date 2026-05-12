---
title: "Networking and content delivery 765"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 770
---

# Networking and content delivery 765

| Improvement opportunity | Solution |
| --- | --- |
| Compute resource features | Elastic Network Interfaces (ENI) used by
Amazon EC2 instances, containers, and
Lambda functions are limited on a per-flow
basis. Review your placement groups to
optimize your EC2 networking throughpu
t. To avoid a bottleneck on a per flow-basi
s, design your application to use multiple
flows. To monitor and get visibility into
your compute related networking metrics,
use CloudWatch Metrics and ethtool. The
ethtool command is included in the ENA
driver and exposes additional network-r
elated metrics that can be published as a
custom metric to CloudWatch.
Amazon Elastic Network Adapters (ENA)
provide further optimization by delivering
better throughput for your instances within a
cluster placement group.
Elastic Fabric Adapter (EFA) is a network
interface for Amazon EC2 instances that
allows you to run workloads requiring high
levels of internode communications at scale
on AWS.
Amazon EBS-optimized instances use an
optimized configuration stack and provide
additional, dedicated capacity to increase the
Amazon EBS I/O. |
