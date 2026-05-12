---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 586
---

# AWS Well-Architected Framework Framework

• What Is Amazon EC2 Auto Scaling?
REL07-BP03 Obtain resources upon detection that more resources are needed for a workload
One of the most valuable features of cloud computing is the ability to provision resources
dynamically.
In traditional on-premises compute environments, you must identify and provision enough
capacity in advance to serve peak demand. This is a problem because it is expensive and because it
poses risks to availability if you underestimate the workload's peak capacity needs.
In the cloud, you don't have to do this. Instead, you can provision compute, database, and other
resource capacity as needed to meet current and forecasted demand. Automated solutions such as
Amazon EC2 Auto Scaling and Application Auto Scaling can bring resources online for you based on
metrics you specify. This can make the scaling process easier and predictable, and it can make your
workload significantly more reliable by ensuring you have enough resources available at all times.
Desired outcome: You configure automatic scaling of compute and other resources to meet
demand. You provide sufficient headroom in your scaling policies to allow bursts of traffic to be
served while additional resources are brought online.


# AWS Well-Architected Framework Framework

Level of risk exposed if this best practice is not established: Medium