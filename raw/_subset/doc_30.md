---
title: "2. For inline inspection solutions:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 370
---

# 2. For inline inspection solutions:

a. If using AWS Network Firewall, create rules, firewall policies, and the firewall itself. Once these
have been configured, you can route traffic to the firewall endpoint to enable inspection.
b. If using a third-party appliance with a Gateway Load Balancer (GWLB), deploy and configure
your appliance in one or more availability zones. Then, create your GWLB, the endpoint
service, endpoint, and configure routing for your traffic.
