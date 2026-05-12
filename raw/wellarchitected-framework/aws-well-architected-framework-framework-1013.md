---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 346
---

# AWS Well-Architected Framework Framework

risk mitigation runbook. For prescriptive guidance on responding to and mitigating the potential
impact of a security incident, see Incident response.
4. Verify that setup has prescriptive guidance or is automated. The external ID is not treated as
a secret, but the external ID must not be an easily guessable value, such as a phone number,
name, or account ID. Make the external ID a read-only field so that the external ID cannot be
changed for the purpose of impersonating the setup.
You or the third party can generate the external ID. Define a process to determine who is
responsible for generating the ID. Regardless of the entity creating the external ID, the third
party enforces uniqueness and formats consistently across customers.
The policy created for cross-account access in your accounts must follow the least-privilege
principle. The third party must provide a role policy document or automated setup mechanism
that uses an AWS CloudFormation template or an equivalent for you. This reduces the chance of
errors associated with manual policy creation and offers an auditable trail. For more information
on using an AWS CloudFormation template to create cross-account roles, see Cross-Account
Roles.
The third party should provide an automated, auditable setup mechanism. However, by using
the role policy document outlining the access needed, you should automate the setup of the
role. Using an AWS CloudFormation template or equivalent, you should monitor for changes
with drift detection as part of the audit practice.
5. Account for changes. Your account structure, your need for the third party, or their service
offering being provided might change. You should anticipate changes and failures, and plan
accordingly with the right people, process, and technology. Audit the level of access you
provide on a periodic basis, and implement detection methods to alert you to unexpected
changes. Monitor and audit the use of the role and the datastore of the external IDs. You should
be prepared to revoke third-party access, either temporarily or permanently, as a result of
unexpected changes or access patterns. Also, measure the impact to your revocation operation,
including the time it takes to perform, the people involved, the cost, and the impact to other
resources.
For prescriptive guidance on detection methods, see the Detection best practices.
