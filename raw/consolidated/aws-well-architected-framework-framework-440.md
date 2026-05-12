---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 577
---

# AWS Well-Architected Framework Framework

4. Look for sharp changes in behavior. An immediate change in quantity or direction of a metric
may indicate that there has been a change in the application or external factors that you may
need to add additional metrics to track.
5. Review whether the current monitoring strategy remains relevant for the application. Based
on an analysis of previous incidents (or the Resilience Analysis Framework), assess if there are
additional aspects of the application that should be incorporated into the monitoring scope.
6. Review your Real User Monitoring (RUM) metrics to determine whether there are any gaps in
application functionality coverage.
7. Review your change management process. Update your procedures if necessary to include a
monitoring analysis step that should be performed before you approve a change.
8. Implement monitoring review as part of your operational readiness review and correction of
error processes.


# AWS Well-Architected Framework Framework

• Using Amazon CloudWatch Dashboards
• AWS Observability Best Practices
• Resilience Analysis Framework
• Resilience Analysis Framework - Observability
• Operational Readiness Review - ORR

# AWS Well-Architected Framework Framework

Level of risk exposed if this best practice is not established: Medium

# AWS Well-Architected Framework Framework

REL 7. How do you design your workload to adapt to changes in demand?
A scalable workload provides elasticity to add or remove resources automatically so that they
closely match the current demand at any given point in time.