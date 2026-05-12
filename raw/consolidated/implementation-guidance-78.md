---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 314
---

# Implementation guidance

Each component or resource of your workload needs to be accessed by administrators, end
users, or other components. Have a clear definition of who or what should have access to each
component, choose the appropriate identity type and method of authentication and authorization.
Regular access to AWS accounts within the organization should be provided using federated access
or a centralized identity provider. You should also centralize your identity management and ensure
that there is an established practice to integrate AWS access to your employee access lifecycle.
For example, when an employee changes to a job role with a different access level, their group
membership should also change to reflect their new access requirements.
When defining access requirements for non-human identities, determine which applications and
components need access and how permissions are granted. Using IAM roles built with the least
