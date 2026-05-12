---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 389
---

# Implementation guidance

When designing a workload, you may be considering ways to protect sensitive data intuitively. For
example, in a multi-tenant application, it is intuitive to think of each tenant's data as sensitive and
put protections in place so that one tenant can't access the data of another tenant. Likewise, you
may intuitively design access controls so only administrators can modify data while other users
have only read-level access or no access at all.
By having these data sensitivity levels defined and captured in policy, along with their data
protection requirements, you can formally identify what data resides in your workload. You can
then determine if the right controls are in place, if the controls can be audited, and what responses
are appropriate if data is found to be mishandled.
To help identify where sensitive data resides within your workload, consider using a data catalog.
A data catalog is a database that maps data in your organization, its location, sensitivity level,
