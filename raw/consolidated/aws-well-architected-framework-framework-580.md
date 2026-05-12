---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 767
---

# AWS Well-Architected Framework Framework

• You stay within one Region because that is where your headquarters is physically located.
• You use firewalls instead of security groups for filtering traffic.
• You break TLS for traffic inspection rather than relying on security groups, endpoint policies, and
other cloud-native functionality.
• You only use subnet-based segmentation instead of security groups.
Benefits of establishing this best practice: Evaluating all service features and options can increase
your workload performance, reduce the cost of infrastructure, decrease the effort required to
maintain your workload, and increase your overall security posture. You can use the global AWS
backbone to provide the optimal networking experience for your customers.
Level of risk exposed if this best practice is not established: High
