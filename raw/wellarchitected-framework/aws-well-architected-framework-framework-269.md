---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 358
---

# AWS Well-Architected Framework Framework

if there are ways you can create mappings across identifiers for these identities, actions, and
resources as the foundation for performing correlation. This can take the form of integrating alert
sources with a security information and event management (SIEM) tool to perform automated
correlation for you, building your own data pipelines and processing, or a combination of both.
An example of a service that can perform correlation for you is Amazon Detective. Detective
performs ongoing ingestion of alerts from various AWS and third-party sources and uses different
forms of intelligence to assemble a visual graph of their relationships to aid investigations.
While the initial criticality of an alert is an aid for prioritization, the context in which the alert
happened determines its true criticality. As an example, Amazon GuardDuty can alert that an
Amazon EC2 instance within your workload is querying an unexpected domain name. GuardDuty
might assign low criticality to this alert on its own. However, automated correlation with other
activity around the time of the alert might uncover that several hundred EC2 instances were
deployed by the same identity, which increases overall operating costs. In this event, this correlated
event context would warrant a new security alert and the criticality might be adjusted to high,
which would expedite further action.
