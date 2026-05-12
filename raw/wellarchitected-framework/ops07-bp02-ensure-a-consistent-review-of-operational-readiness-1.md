---
title: "OPS07-BP02 Ensure a consistent review of operational readiness"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 188
---

# OPS07-BP02 Ensure a consistent review of operational readiness

Use Operational Readiness Reviews (ORRs) to validate that you can operate your workload. ORR is
a mechanism developed at Amazon to validate that teams can safely operate their workloads. An
ORR is a review and inspection process using a checklist of requirements. An ORR is a self-service
experience that teams use to certify their workloads. ORRs include best practices from lessons
learned from our years of building software.
An ORR checklist is composed of architectural recommendations, operational process, event
management, and release quality. Our Correction of Error (CoE) process is a major driver of these
items. Your own post-incident analysis should drive the evolution of your own ORR. An ORR is
not only about following best practices but preventing the recurrence of events that you’ve seen
before. Lastly, security, governance, and compliance requirements can also be included in an ORR.
Run ORRs before a workload launches to general availability and then throughout the software
development lifecycle. Running the ORR before launch increases your ability to operate the
workload safely. Periodically re-run your ORR on the workload to catch any drift from best
practices. You can have ORR checklists for new services launches and ORRs for periodic reviews.
This helps keep you up to date on new best practices that arise and incorporate lessons learned
from post-incident analysis. As your use of the cloud matures, you can build ORR requirements into
your architecture as defaults.
Desired outcome: You have an ORR checklist with best practices for your organization. ORRs are
conducted before workloads launch. ORRs are run periodically over the course of the workload
lifecycle.
