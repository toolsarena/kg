---
title: "Lambda functions are limited on a per-flow"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 770
---

# Lambda functions are limited on a per-flow

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


# Lambda

• AWS re:Invent 2022 - Designing event-driven integrations using Amazon EventBridge
• AWS re:Invent 2017: Elastic Load Balancing Deep Dive and Best Practices