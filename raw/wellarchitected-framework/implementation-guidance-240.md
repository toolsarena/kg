---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 863
---

# Implementation guidance

Cost optimization means delivering business outcomes at the lowest price point, which can only
be achieved by allocating workload costs based on workload metrics (measured by workload
efficiency). Monitor the defined workload metrics through log files or other application monitoring.
Combine this data with the workload’s costs, which can be obtained by looking at costs with
a specific tag value or account ID. Perform this analysis at the hourly level. Your efficiency
typically changes if you have static cost components (for example, a backend database running
permanently) with a varying request rate (for example, usage peaks at nine in the morning to five
in the evening, with few requests at night). Understanding the relationship between the static and
variable costs helps you focus your optimization activities.
