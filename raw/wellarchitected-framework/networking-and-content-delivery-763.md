---
title: "Networking and content delivery 763"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 768
---

# Networking and content delivery 763

| Improvement opportunity | Solution |
| --- | --- |
| Network path or routes | Use Network Access Analyzer to identify
paths or routes. |
| Network protocols | See PERF04-BP05 Choose network protocols
to improve performance |
| Network topology | Evaluate your operational and performan
ce tradeoffs between VPC Peering and AWS
Transit Gateway when connecting multiple
accounts. AWS Transit Gateway simplifie
s how you interconnect all of your VPCs,
which can span across thousands of AWS
accounts and into on-premises networks.
Share your AWS Transit Gateway between
multiple accounts using AWS Resource Access
Manager.
See PERF04-BP03 Choose appropriate
dedicated connectivity or VPN for your
workload |
| Network services | AWS Global Accelerator is a networking
service that improves the performance of
your users’ traffic by up to 60% using the
AWS global network infrastructure. |
