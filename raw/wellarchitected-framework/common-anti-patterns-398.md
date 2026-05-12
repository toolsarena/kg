---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 700
---

# Common anti-patterns:

• You fail to update recovery locations when changes are made to the primary locations, which
results in outdated configurations that could hinder recovery efforts.
• You do not consider potential limitations such as service differences between primary and
recovery locations, which can lead to unexpected failures during failover.
• You rely on manual processes to update and synchronize the DR environment, which increases
the risk of human error and inconsistency.
• You fail to detect configuration drift, which leads to a false sense of DR site readiness prior to an
incident.
Benefits of establishing this best practice: Consistency between the DR environment and the
primary environment significantly improves the likelihood of a successful recovery after an incident
and reduces the risk of a failed recovery procedure.
Level of risk exposed if this best practice is not established: High
