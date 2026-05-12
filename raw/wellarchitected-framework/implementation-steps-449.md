---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 870
---

# Implementation steps

• Implement Amazon EC2 Auto Scaling or Application Auto Scaling: For resources that are
supported, configure them with Amazon EC2 Auto Scaling or Application Auto Scaling. These
services can help you optimize your utilization and cost efficiencies when consuming AWS
services. When demand drops, these services will automatically remove any excess resource
capacity so you avoid overspending.
• Configure CloudWatch to terminate instances: Instances can be configured to terminate
using CloudWatch alarms. Using the metrics from the decommissioning process, implement an
alarm with an Amazon Elastic Compute Cloud action. Verify the operation in a non-production
environment before rolling out.
