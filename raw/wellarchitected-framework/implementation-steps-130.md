---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 634
---

# Implementation steps

• Your monitoring interval is dependent on how quickly you must recover. Your recovery time
is driven by the time it takes to recover, so you must determine the frequency of collection by
accounting for this time and your recovery time objective (RTO).
• Configure detailed monitoring for components and managed services.
• Determine if detailed monitoring for EC2 instances and Auto Scaling is necessary. Detailed
monitoring provides one minute interval metrics, and default monitoring provides five minute
interval metrics.
• Determine if enhanced monitoring for RDS is necessary. Enhanced monitoring uses an agent
on RDS instances to get useful information about different process or threads.
• Determine the monitoring requirements of critical serverless components for Lambda, API
Gateway, Amazon EKS, Amazon ECS, and all types of load balancers.
• Determine the monitoring requirements of storage components for Amazon S3, Amazon FSx,
Amazon EFS, and Amazon EBS.
• Create custom metrics to measure business key performance indicators (KPIs). Workloads
implement key business functions, which should be used as KPIs that help identify when an
indirect problem happens.
• Monitor the user experience for failures using user canaries. Synthetic transaction testing (also
known as canary testing, but not to be confused with canary deployments) that can run and
simulate customer behavior is among the most important testing processes. Run these tests
constantly against your workload endpoints from diverse remote locations.
• Create custom metrics that track the user's experience. If you can instrument the experience of
the customer, you can determine when the consumer experience degrades.
