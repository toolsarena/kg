---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 369
---

# Implementation guidance

Have fine-grained control over both your stateful and stateless network traffic using AWS Network
Firewall, or other Firewalls and Intrusion Prevention Systems (IPS) on AWS Marketplace that you
can deploy behind a Gateway Load Balancer (GWLB). AWS Network Firewall supports Suricata-
compatible open source IPS specifications to help protect your workload.
Both the AWS Network Firewall and vendor solutions that use a GWLB support different inline
inspection deployment models. For example, you can perform inspection on a per-VPC basis,
