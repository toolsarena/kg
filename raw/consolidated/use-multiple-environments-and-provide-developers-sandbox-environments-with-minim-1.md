---
title: "Use multiple environments and provide developers sandbox environments with minimized"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 170
---

# Use multiple environments and provide developers sandbox environments with minimized

controls to aid in experimentation. Provide individual development environments to help
work in parallel, increasing development agility. Implement more rigorous controls in the
environments approaching production to allow developers to innovate. Use infrastructure as code
and configuration management systems to deploy environments that are configured consistent
with the controls present in production to ensure systems operate as expected when deployed.
When environments are not in use, turn them off to avoid costs associated with idle resources
(for example, development systems on evenings and weekends). Deploy production equivalent
environments when load testing to improve valid results.
Teams such as platform engineering, networking, and security operations often manage capabilies
at the organization level with distinct requirements. A separation of accounts alone is insufficient
to provide and maintain separate environments for experimentation, development, and testing. In
such cases, create separate instances of AWS Organizations.
