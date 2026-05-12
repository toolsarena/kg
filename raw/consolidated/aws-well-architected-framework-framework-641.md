---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 847
---

# AWS Well-Architected Framework Framework

the type of resources that can be created, and where they can be created. This minimizes the
possibility of resources being created outside of the defined policy. Use the roles and groups
created previously and assign IAM policies to enforce the correct usage. SCP offers central control
over the maximum available permissions for all accounts in your organization, keeping your
accounts stay within your access control guidelines. SCPs are available only in an organization
that has all features turned on, and you can configure the SCPs to either deny or allow actions for
member accounts by default. For more details on implementing access management, see the Well-
Architected Security Pillar whitepaper.
Governance can also be implemented through management of AWS service quotas. By
ensuring service quotas are set with minimum overhead and accurately maintained, you can
minimize resource creation outside of your organization’s requirements. To achieve this, you
must understand how quickly your requirements can change, understand projects in progress
(both creation and decommission of resources), and factor in how fast quota changes can be
implemented. Service quotas can be used to increase your quotas when required.
