---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 977
---

# Implementation steps

• Use proximity: Consider proximity to the data or users as a decision factor when selecting a
Region for your workload.
• Partition services: Partition Regionally-consumed services so that their Region-specific data is
stored within the Region where it is consumed.
• Use efficient file formats: Use efficient file formats (such as Parquet or ORC) and compress data
before you move it over the network.
• Minimize data movement: Don't move unused data. Some examples that can help you avoid
moving unused data:
• Reduce API responses to only relevant data.
