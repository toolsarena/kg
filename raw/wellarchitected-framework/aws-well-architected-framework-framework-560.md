---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 736
---

# AWS Well-Architected Framework Framework

• The metric value must increase or decrease proportionally to the number of instances in the
Auto Scaling group.
• Make sure that you use dynamic scaling instead of manual scaling for your Auto Scaling group.
We also recommend that you use target tracking scaling policies in your dynamic scaling.
• Verify that workload deployments can handle both scaling events (up and down). As an example,
you can use Activity history to verify a scaling activity for an Auto Scaling group.
• Evaluate your workload for predictable patterns and proactively scale as you anticipate predicted
and planned changes in demand. With predictive scaling, you can eliminate the need to
overprovision capacity. For more detail, see Predictive Scaling with Amazon EC2 Auto Scaling.
