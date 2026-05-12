---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 646
---

# AWS Well-Architected Framework Framework

• Route 53 Health checks for more automated updates
Consider some services in a secondary Region, if the service is mission critical, to allow for more
control plane and data plane actions in an unaffected Region.
• Amazon EC2 Auto Scaling or Amazon EKS in a primary Region compared to Amazon EC2 Auto
Scaling or Amazon EKS in a secondary Region and routing traffic to secondary Region (control
plane action)
• Make read replica in secondary primary or attempting same action in primary Region (control
plane action)
