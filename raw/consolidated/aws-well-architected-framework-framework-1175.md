---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 555
---

# AWS Well-Architected Framework Framework

In addition to server replacement, another benefit of stateless applications is that they can scale
horizontally because any of the available compute resources (such as EC2 instances and AWS
Lambda functions) can service any request.
Benefits of establishing this best practice: Systems that are designed to be stateless are more
adaptable to horizontal scaling, making it possible to add or remove capacity based on fluctuating
traffic and demand. They are also inherently resilient to failures and provide flexibility and agility in
application development.
Level of risk exposed if this best practice is not established: Medium


# AWS Well-Architected Framework Framework

• Design a stateless architecture after you identify which state and user data need to be persisted
with your storage solution of choice.