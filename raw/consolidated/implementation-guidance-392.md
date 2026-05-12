---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 372
---

# Implementation guidance

A number of network protection controls described in SEC05-BP02 Control traffic flows within
your network layers and SEC05-BP03 Implement inspection-based protection come with managed
rules systems that can update automatically based on the latest threat intelligence. Examples
of protecting your web endpoints include AWS WAF managed rules and AWS Shield Advanced
automatic application layer DDoS mitigation. Use AWS Network Firewall managed rule groups to
stay up to date with low-reputation domain lists and threat signatures as well.
Beyond managed rules, we recommend you use DevOps practices to automate deploying your
network resources, protections, and the rules you specify. You can capture these definitions in
