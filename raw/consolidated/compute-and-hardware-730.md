---
title: "Compute and hardware 730"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 735
---

# Compute and hardware 730

| Autoscaling Mechanism | Where to use |
| --- | --- |
| Amazon EC2 Auto Scaling | To ensure you have the correct number of
Amazon EC2 instances available to handle
the user load for your application. |
| Application Auto Scaling | To automatically scale the resources for
individual AWS services beyond Amazon EC2
such as AWS Lambda functions or Amazon
Elastic Container Service (Amazon ECS)
services. |
| Kubernetes Cluster Autoscaler/Karpenter | To automatically scale Kubernetes clusters. |
