---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 897
---

# AWS Well-Architected Framework Framework

Analyze your Amazon EC2 and Amazon RDS instances whether they can be turned off when you
don’t use (after hours and weekends). This approach will allow you to reduce costs by 70% or more
compared to using them 24/7. If you have Amazon Redshift clusters that only need to be available
at specific times, you can pause the cluster and later resume it. When the Amazon Redshift cluster
or Amazon EC2 and Amazon RDS Instance is stopped, the compute billing halts and only the
storage charge applies.
Note that On-Demand Capacity reservations (ODCR) are not a pricing discount. Capacity
Reservations are charged at the equivalent On-Demand rate, whether you run instances in reserved
capacity or not. They should be considered when you need to provide enough capacity for the
resources you plan to run. ODCRs don't have to be tied to long-term commitments, as they can
be cancelled when you no longer need them, but they can also benefit from the discounts that
Savings Plans or Reserved Instances provide.


# AWS Well-Architected Framework Framework

• Instance purchasing options
• AWS Enterprise