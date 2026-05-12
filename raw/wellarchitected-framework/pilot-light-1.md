---
title: "Pilot light"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 689
---

# Pilot light

With the pilot light approach, you replicate your data from your primary Region to your recovery
Region. Core resources used for the workload infrastructure are deployed in the recovery Region,
however additional resources and any dependencies are still needed to make this a functional
stack. For example, in Figure 20, no compute instances are deployed.
