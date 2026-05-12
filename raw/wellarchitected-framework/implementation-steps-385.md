---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 649
---

# Implementation steps

• Build systems that are statically stable and operate in only one mode. In this case, provision
enough instances in each Availability Zone or Region to handle the workload capacity if one
Availability Zone or Region were removed. A variety of services can be used for routing to
healthy resources, such as:
