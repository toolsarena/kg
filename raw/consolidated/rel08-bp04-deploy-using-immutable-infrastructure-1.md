---
title: "REL08-BP04 Deploy using immutable infrastructure"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 598
---

# REL08-BP04 Deploy using immutable infrastructure

Immutable infrastructure is a model that mandates that no updates, security patches, or
configuration changes happen in-place on production workloads. When a change is needed, the
architecture is built onto new infrastructure and deployed into production.
Follow an immutable infrastructure deployment strategy to increase the reliability, consistency,
and reproducibility in your workload deployments.
Desired outcome: With immutable infrastructure, no in-place modifications are allowed to run
infrastructure resources within a workload. Instead, when a change is needed, a new set of updated
infrastructure resources containing all the necessary changes are deployed in parallel to your
existing resources. This deployment is validated automatically, and if successful, traffic is gradually
shifted to the new set of resources.
This deployment strategy applies to software updates, security patches, infrastructure changes,
configuration updates, and application updates, among others.
