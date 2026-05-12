---
title: "1. Scope permissions based on groups and attributes:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 312
---

# 1. Scope permissions based on groups and attributes:

a. Consider including conditions in your permission policies that compare the attributes of your
principal with the attributes of the resources being accessed. For example, you can define a
condition to allow access to a resource only if the value of a PrincipalTag condition key
matches the value of a ResourceTag key of the same name.
b. When defining ABAC policies, follow the guidance in the ABAC authorization best practices
and examples.
