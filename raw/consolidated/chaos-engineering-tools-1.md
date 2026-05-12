---
title: "Chaos engineering tools:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 667
---

# Chaos engineering tools:

AWS Fault Injection Service (AWS FIS) is a fully managed service for running fault injection
experiments that can be used as part of your CD pipeline, or outside of the pipeline. AWS FIS is a
good choice to use during chaos engineering game days. It supports simultaneously introducing
faults across different types of resources including Amazon EC2, Amazon Elastic Container Service
(Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), and Amazon RDS. These faults
include termination of resources, forcing failovers, stressing CPU or memory, throttling, latency,
and packet loss. Since it is integrated with Amazon CloudWatch Alarms, you can set up stop
conditions as guardrails to rollback an experiment if it causes unexpected impact.
