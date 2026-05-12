---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 865
---

# Implementation steps

• Implement a tagging scheme: Implement a tagging scheme that identifies the workload the
resource belongs to, verifying that all resources within the workload are tagged accordingly.
Tagging helps you categorize resources by purpose, team, environment, or other criteria relevant
to your business. For more detail on tagging uses cases, strategies, and techniques, see AWS
Tagging Best Practices.
• Implement workload throughput or output monitoring: Implement workload throughput
monitoring or alarming, initiating on either input requests or output completions. Configure it to
provide notifications when workload requests or outputs drop to zero, indicating the workload
resources are no longer used. Incorporate a time factor if the workload periodically drops to zero
under normal conditions. For more detail on unused or underutilized resources, see AWS Trusted
Advisor Cost Optimization checks.
• Group AWS resources: Create groups for AWS resources. You can use AWS Resource Groups to
organize and manage your AWS resources that are in the same AWS Region. You can add tags to
