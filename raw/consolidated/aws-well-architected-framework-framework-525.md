---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 678
---

# AWS Well-Architected Framework Framework

To help you reproduce real-world scenarios where system components or services may fail
unexpectedly, inject simulated faults as a game day exercise. Teams can test the resilience and
fault tolerance of their systems and simulate their incident response and recovery processes in a
controlled environment.
In AWS, your game days can be carried out with replicas of your production environment using
infrastructure as code. Through this process, you can test in a safe environment that closely
resembles your production environment. Consider AWS Fault Injection Service to create different
failure scenarios. Use services like Amazon CloudWatch and AWS X-Ray to monitor system behavior
during game days. Use AWS Systems Manager to manage and run playbooks, and use AWS Step
Functions to orchestrate recurring game day workflows.


# AWS Well-Architected Framework Framework

• REL12-BP04 Test resiliency using chaos engineering
• OPS04-BP01 Identify key performance indicators
• OPS07-BP03 Use runbooks to perform procedures
• OPS10-BP01 Use a process for event, incident, and problem management