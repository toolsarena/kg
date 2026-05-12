---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 628
---

# AWS Well-Architected Framework Framework

1. Implement self-healing. Deploy your instances or containers using automatic scaling when
possible. If you cannot use automatic scaling, use automatic recovery for EC2 instances or
implement self-healing automation based on Amazon EC2 or ECS container lifecycle events.
• Use Amazon EC2 Auto Scaling groups for instances and container workloads that have no
requirements for a single instance IP address, private IP address, Elastic IP address, and
instance metadata.
• The launch template user data can be used to implement automation that can self-heal
most workloads.
• Use automatic recovery of Amazon EC2 instances for workloads that require a single instance
ID address, private IP address, elastic IP address, and instance metadata.
• Automatic Recovery will send recovery status alerts to a SNS topic as the instance failure is
detected.
• Use Amazon EC2 instance lifecycle events or Amazon ECS events to automate self-healing
where automatic scaling or EC2 recovery cannot be used.
• Use the events to invoke automation that will heal your component according to the
process logic you require.
• Protect stateful workloads that are limited to a single location using AWS Elastic Disaster
Recovery.
