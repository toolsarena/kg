---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 220
---

# Common anti-patterns:

• A workload goes down, leaving a service unavailable. Call volumes spike as users request to
know what's going on. Managers add to the volume requesting to know who's working an issue.
Various operations teams duplicate efforts in trying to investigate.
• A desire for a new capability leads to several personnel being reassigned to an engineering
effort. No backfill is provided, and issue resolution times spike. This information is not captured,
and only after several weeks and dissatisfied user feedback does leadership become aware of the
issue.
Benefits of establishing this best practice: During operational events where the business is
impacted, much time and energy can be wasted querying information from various teams
attempting to understand the situation. By establishing widely-disseminated status pages and
dashboards, stakeholders can quickly obtain information such as whether or not an issue was
detected, who has lead on the issue, or when a return to normal operations may be expected. This
frees team members from spending too much time communicating status to others and more time
addressing issues.
In addition, dashboards and reports can provide insights to decision-makers and stakeholders to
see how operations teams are able to respond to business needs and how their resources are being
allocated. This is crucial for determining if adequate resources are in place to support the business.
Level of risk exposed if this best practice is not established: Medium
