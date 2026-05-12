---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 985
---

# AWS Well-Architected Framework Framework

• For machine learning workloads, take advantage of purpose-built hardware that is specific to
your workload such as AWS Trainium, AWS Inferentia, and Amazon EC2 DL1. AWS Inferentia
instances such as Inf2 instances offer up to 50% better performance per watt over comparable
Amazon EC2 instances.
• Use Amazon SageMaker AI Inference Recommender to right size ML inference endpoint.
• For spiky workloads (workloads with infrequent requirements for additional capacity), use
burstable performance instances.
• For stateless and fault-tolerant workloads, use Amazon EC2 Spot Instances to increase overall
utilization of the cloud, and reduce the sustainability impact of unused resources.
• Operate and optimize: Operate and optimize your workload instance.
• For ephemeral workloads, evaluate instance Amazon CloudWatch metrics such as
CPUUtilization to identify if the instance is idle or under-utilized.
• For stable workloads, check AWS rightsizing tools such as AWS Compute Optimizer at regular
intervals to identify opportunities to optimize and right-size the instances. For further
examples and recommendations, see the following labs:
• Well-Architected Lab - Rightsizing Recommendations
• Well-Architected Lab - Rightsizing with Compute Optimizer
• Well-Architected Lab - Optimize Hardware Patterns and Observice Sustainability KPIs
