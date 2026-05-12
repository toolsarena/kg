---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 587
---

# Implementation guidance

First, determine whether the workload component is suitable for automatic scaling. These
components are called horizontally scalable because they provide the same resources and
behave identically. Examples of horizontally-scalable components include EC2 instances that
are configured alike, Amazon Elastic Container Service (ECS) tasks, and pods running on Amazon
Elastic Kubernetes Service (EKS). These compute resources are typically located behind a load
balancer and are referred to as replicas.
Other replicated resources may include database read replicas, Amazon DynamoDB tables, and
Amazon ElastiCache (Redis OSS) clusters. For a complete list of supported resources, see AWS
services that you can use with Application Auto Scaling.
For container-based architectures, you may need to scale two different ways. First, you may need
to scale the containers that provide horizontally-scalable services. Second, you may need to scale
the compute resources to make space for new containers. Different automatic scaling mechanisms
exist for each layer. To scale ECS tasks, you can use Application Auto Scaling. To scale Kubernetes
pods, you can use Horizontal Pod Autoscaler (HPA) or Kubernetes Event-driven Autoscaling (KEDA).
To scale the compute resources, you can use Capacity Providers for ECS, or for Kubernetes, you can
use Karpenter or Cluster Autoscaler.
Next, select how you will perform automatic scaling. There are three major options: metric-based
scaling, scheduled scaling, and predictive scaling.
