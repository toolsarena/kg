---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 370
---

# AWS Well-Architected Framework Framework

centralize in an inspection VPC, or deploy in a hybrid model where east-west traffic flows through
an inspection VPC and Internet ingress is inspected per-VPC. Another consideration is whether
the solution supports unwrapping Transport Layer Security (TLS), enabling deep packet inspection
for traffic flows initiated in either direction. For more information and in-depth details on these
configurations, see the AWS Network Firewall Best Practice guide.
If you are using solutions that perform out-of-band inspections, such as pcap analysis of packet
data from network interfaces operating in promiscuous mode, you can configure VPC traffic
mirroring. Mirrored traffic counts towards the available bandwidth of your interfaces and is subject
to the same data transfer charges as non-mirrored traffic. You can see if virtual versions of these
appliances are available on the AWS Marketplace, which may support inline deployment behind a
