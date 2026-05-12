---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 672
---

# AWS Well-Architected Framework Framework

with the experiment. There are several options for injecting the faults. For workloads on
AWS, AWS FIS provides many predefined fault simulations called actions. You can also define
custom actions that run in AWS FIS using AWS Systems Manager documents.
We discourage the use of custom scripts for chaos experiments, unless the scripts have
the capabilities to understand the current state of the workload, are able to emit logs, and
provide mechanisms for rollbacks and stop conditions where possible.
An effective framework or toolset which supports chaos engineering should track the current
state of an experiment, emit logs, and provide rollback mechanisms to support the controlled
running of an experiment. Start with an established service like AWS FIS that allows you
to perform experiments with a clearly defined scope and safety mechanisms that rollback
the experiment if the experiment introduces unexpected turbulence. To learn about a wider
variety of experiments using AWS FIS, also see the Resilient and Well-Architected Apps with
Chaos Engineering lab. Also, AWS Resilience Hub will analyze your workload and create
experiments that you can choose to implement and run in AWS FIS.
