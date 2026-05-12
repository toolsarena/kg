---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 680
---

# Common anti-patterns:

• You haven't designated recovery objectives.
• You select arbitrary recovery objectives.
• You select recovery objectives that are too lenient and do not meet business objectives.
• You have not evaluated the impact of downtime and data loss.
• You select unrealistic recovery objectives, such as zero time to recover or zero data loss, which
may not be achievable for your workload configuration.
• You select recovery objectives that are more stringent than actual business objectives. This forces
recovery implementations that are costlier and more complicated than what the workload needs.
• You select recovery objectives that are incompatible with those of a dependent workload.
• You fail to consider regulatory and compliance requirements.
Benefits of establishing this best practice: When you set RTOs and RPOs for your workloads, you
establish clear and measurable goals for recovery based on your business needs. Once you've set
those goals, you can create disaster recovery (DR) plans that are tailored to meet them.
Level of risk exposed if this best practice is not established: High
