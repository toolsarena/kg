---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 363
---

# Common anti-patterns:

• You create all resources in a single VPC or subnet.
• You construct your network layers without consideration of data sensitivity requirements,
component behaviors, or functionality.
• You use VPCs and subnets as defaults for all network layer considerations, and you don't
consider how AWS managed services influence your topology.
Benefits of establishing this best practice: Establishing network layers is the first step in
restricting unnecessary pathways through the network, particularly those that lead to critical
systems and data. This makes it harder for unauthorized actors to gain access to your network and
navigate to additional resources within. Discrete network layers beneficially reduce the scope of
