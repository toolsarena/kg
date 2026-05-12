---
title: "OPS05-BP03 Use configuration management systems"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 154
---

# OPS05-BP03 Use configuration management systems

Use configuration management systems to make and track configuration changes. These systems
reduce errors caused by manual processes and reduce the level of effort to deploy changes.
Static configuration management sets values when initializing a resource that are expected
to remain consistent throughout the resource’s lifetime. Dynamic configuration management
sets values at initialization that can or are expected to change during the lifetime of a resource.
For example, you could set a feature toggle to activate functionality in your code through a
configuration change, or change the level of log detail during an incident.
Configurations should be deployed in a known and consistent state. You should use automated
inspection to continually monitor resource configurations across environments and regions.
These controls should be defined as code and management automated to ensure rules are
consistently appplied across environments. Changes to configurations should be updated through
agreed change control procedures and applied consistently, honoring version control. Application
