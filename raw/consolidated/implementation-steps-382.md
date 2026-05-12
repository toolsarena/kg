---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 638
---

# Implementation steps

• Create failover designs for all appropriate applications and services. Isolate each architecture
component and create failover designs meeting RTO and RPO for each component.
• Configure lower environments (like development or test) with all services that are required
to have a failover plan. Deploy the solutions using infrastructure as code (IaC) to ensure
repeatability.
• Configure a recovery site such as a second Region to implement and test the failover designs. If
necessary, resources for testing can be configured temporarily to limit additional costs.
• Determine which failover plans are automated by AWS, which can be automated by a DevOps
process, and which might be manual. Document and measure each service's RTO and RPO.
• Create a failover playbook and include all steps to failover each resource, application, and
service.
• Create a failback playbook and include all steps to failback (with timing) each resource,
application, and service
• Create a plan to initiate and rehearse the playbook. Use simulations and chaos testing to test the
playbook steps and automation.
