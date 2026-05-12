---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 500
---

# AWS Well-Architected Framework Framework

In addition to physical redundancy with multiple AWS Direct Connect connections and multiple
VPN tunnels (or a combination of both), implementing Border Gateway Protocol (BGP) dynamic
routing is also crucial. Dynamic BGP provides automatic rerouting of traffic from one path to
another based on real-time network conditions and configured policies. This dynamic behavior
is especially beneficial in maintaining network availability and service continuity in the event of
link or network failures. It quickly selects alternative paths, enhancing the network's resilience and
reliability.
