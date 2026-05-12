---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 989
---

# Implementation steps

• Explore compute accelerators: Identify which accelerated computing instances can address your
requirements.
• Use purpose-built hardware: For machine learning workloads, take advantage of purpose-built
hardware that is specific to your workload, such as AWS Trainium, AWS Inferentia, and Amazon
EC2 DL1. AWS Inferentia instances such as Inf2 instances offer up to 50% better performance per
watt over comparable Amazon EC2 instances.
• Monitor usage metrics: Collect usage metric for your accelerated computing instances. For
example, you can use CloudWatch agent to collect metrics such as utilization_gpu and
utilization_memory for your GPUs as shown in Collect NVIDIA GPU metrics with Amazon
CloudWatch.
• Rightsize: Optimize the code, network operation, and settings of hardware accelerators to make
sure that underlying hardware is fully utilized.
• Optimize GPU settings
• GPU Monitoring and Optimization in the Deep Learning AMI
• Optimizing I/O for GPU performance tuning of deep learning training in Amazon SageMaker
