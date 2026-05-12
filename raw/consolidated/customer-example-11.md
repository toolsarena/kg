---
title: "Customer example"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 177
---

# Customer example

As part of their continuous integration and continuous delivery (CI/CD) pipeline, AnyCompany
Retail performs the defined steps needed to release infrastructure and software updates for its
customers in a production-like environment. The pipeline is comprised of pre-checks to detect drift
(detecting changes to resources performed outside of your IaC) in resources prior to deployment,
as well as validate actions that the IaC takes upon its initiation. It validates deployment steps, like
verifying that certain files and configurations are in place and services are in running states and are
responding correctly to health checks on local host before re-registering with the load balancer.
Additionally, all changes flag a number of automated tests, such as functional, security, regression,
integration, and load tests.


# Customer example

AnyCompany Retail is on a mission to achieve minimal to zero downtime deployments, meaning
that there's no perceivable impact to its users during deployments. To accomplish this, the
company has established deployment patterns (see the following workflow diagram), such as