---
title: "Compute and hardware"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 47
---

# Compute and hardware

The optimal compute choice for a particular workload can vary based on application design, usage
patterns, and configuration settings. Architectures may use different compute choices for various
components and allow different features to improve performance. Selecting the wrong compute
choice for an architecture can lead to lower performance efficiency.
In AWS, compute is available in three forms: instances, containers, and functions:
• Instances are virtualized servers, permitting you to change their capabilities with a button or an
API call. Because resource decisions in the cloud aren’t fixed, you can experiment with different
server types. At AWS, these virtual server instances come in different families and sizes, and they
offer a wide variety of capabilities, including solid-state drives (SSDs) and graphics processing
units (GPUs).
• Containers are a method of operating system virtualization that permit you to run an application
and its dependencies in resource-isolated processes. AWS Fargate is serverless compute for
containers or Amazon EC2 can be used if you need control over the installation, configuration,
and management of your compute environment. You can also choose from multiple container
orchestration platforms: Amazon Elastic Container Service (ECS) or Amazon Elastic Kubernetes
Service (EKS).
• Functions abstract the run environment from the code you want to apply. For example, AWS
Lambda permits you to run code without running an instance.
The following question focuses on these considerations for performance efficiency.
PERF 2: How do you select and use compute resources in your workload?
The more efficient compute solution for a workload varies based on application design, usage
patterns, and configuration settings. Architectures can use different compute solutions for
various components and turn on different features to improve performance. Selecting the
wrong compute solution for an architecture can lead to lower performance efficiency.
