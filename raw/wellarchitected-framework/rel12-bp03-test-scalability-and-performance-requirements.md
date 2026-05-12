---
title: "REL12-BP03 Test scalability and performance requirements"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 661
---

# REL12-BP03 Test scalability and performance requirements

Use techniques such as load testing to validate that the workload meets scaling and performance
requirements.
In the cloud, you can create a production-scale test environment for your workload on demand.
Instead of reliance on a scaled-down test environment, which could lead to inaccurate predictions
of production behaviors, you can use the cloud to provision a test environment that closely mirrors
your expected production environment. This environment helps you test in a more accurate
simulation of the real-world conditions your application faces.
Alongside your performance testing efforts, it's essential to validate that your base resources,
scaling settings, service quotas, and resiliency design operate as expected under load. This holistic
