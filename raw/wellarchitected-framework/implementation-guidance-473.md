---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 648
---

# Implementation guidance

Bimodal behavior occurs when your workload exhibits different behavior under normal and failure
modes (for example, relying on launching new instances if an Availability Zone fails). An example
of bimodal behavior is when stable Amazon EC2 designs provision enough instances in each
Availability Zone to handle the workload load if one AZ were removed. Elastic Load Balancing or
Amazon Route 53 health would check to shift a load away from the impaired instances. After traffic
has shifted, use AWS Auto Scaling to asynchronously replace instances from the failed zone and
launch them in the healthy zones. Static stability for compute deployment (such as EC2 instances
or containers) results in the highest reliability.
