---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 737
---

# Implementation guidance

Accelerated computing instances provide access to hardware-based compute accelerators such as
GPUs and FPGAs. These hardware accelerators perform certain functions like graphic processing or
data pattern matching more efficiently than CPU-based alternatives. Many accelerated workloads,
such as rendering, transcoding, and machine learning, are highly variable in terms of resource
usage. Only run this hardware for the time needed, and decommission them with automation when
not required to improve overall performance efficiency.
