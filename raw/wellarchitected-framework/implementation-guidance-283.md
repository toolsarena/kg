---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 969
---

# Implementation guidance

Datasets usually have different retention and access requirements during their lifecycle. For
example, your application may need frequent access to some datasets for a limited period of time.
After that, those datasets are infrequently accessed. To improve the efficiency of data storage
and computation over time, implement lifecycle policies, which are rules that define how data is
handled over time.
With lifecycle configuration rules, you can tell the specific storage service to transition a dataset
to more energy-efficient storage tiers, archive it, or delete it. This practice minimizes active data
storage and retrieval, which leads to lower energy consumption. In addition, practices such as
archiving or deleting obsolete data support regulatory compliance and data governance.
