---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 650
---

# AWS Well-Architected Framework Framework

• Cross Region DNS Routing
• MRAP Amazon S3 MultiRegion Routing
• AWS Global Accelerator
• Amazon Application Recovery Controller
• Configure database read replicas to account for the loss of a single primary instance or a read
replica. If traffic is being served by read replicas, the quantity in each Availability Zone and each
Region should equate to the overall need in case of the zone or Region failure.
• Configure critical data in Amazon S3 storage that is designed to be statically stable for data
stored in case of an Availability Zone failure. If Amazon S3 One Zone-IA storage class is used, this
should not be considered statically stable, as the loss of that zone minimizes access to this stored
data.
• Load balancers are sometimes configured incorrectly or by design to service a specific Availability
Zone. In this case, the statically stable design might be to spread a workload across multiple
AZs in a more complex design. The original design may be used to reduce interzone traffic for
security, latency, or cost reasons.


# AWS Well-Architected Framework Framework

• AWS Global Accelerator
• Amazon Application Recovery Controller
• Single Zone Amazon S3
• Cross Zone Load Balancing