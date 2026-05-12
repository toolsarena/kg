---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 772
---

# Implementation guidance

Develop a hybrid networking architecture based on your bandwidth requirements. Direct Connect
allows you to connect your on-premises network privately with AWS. It is suitable when you need
high-bandwidth and low-latency while achieving consistent performance. A VPN connection
establishes secure connection over the internet. It is used when only a temporary connection is
required, when cost is a factor, or as a contingency while waiting for resilient physical network
connectivity to be established when using Direct Connect.
If your bandwidth requirements are high, you might consider multiple Direct Connect or VPN
services. Traffic can be load balanced across services, although we don't recommend load balancing
between Direct Connect and VPN because of the latency and bandwidth differences.
