---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 989
---

# Implementation guidance

If you require high processing capability, you can benefit from using accelerated computing
instances, which provide access to hardware-based compute accelerators such as graphics
processing units (GPUs) and field programmable gate arrays (FPGAs). These hardware accelerators
perform certain functions like graphic processing or data pattern matching more efficiently
than CPU-based alternatives. Many accelerated workloads, such as rendering, transcoding, and
machine learning, are highly variable in terms of resource usage. Only run this hardware for the
time needed, and decommission them with automation when not required to minimize resources
consumed.
