---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 476
---

# AWS Well-Architected Framework Framework

• Not considering the effect of resiliency architectures (like active or passive) in future quota needs
during a degradation in the non-primary Region.
• Not evaluating quotas regularly and making necessary changes in every Region and account the
workload runs.
• Not leveraging quota request templates to request increases across multiple Regions and
accounts.
• Not updating service quotas due to incorrectly thinking that increasing quotas has cost
implications like compute reservation requests.
Benefits of establishing this best practice: Verifying that you can handle your current load in
secondary regions or accounts if regional services become unavailable. This can help reduce the
number of errors or levels of degradations that occur during region loss.
Level of risk exposed if this best practice is not established: High
