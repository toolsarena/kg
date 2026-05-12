---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 843
---

# AWS Well-Architected Framework Framework

and specify whether the workload or workload environment should be separate from other
workloads. Security promotes adhesion to access and data requirements. Reliability manages
limits so that environments and workloads do not impact others. Review the security and
reliability pillars of the Well-Architected Framework periodically and follow the provided best
practices. Financial constructs create strict financial separation (different cost center, workload
ownerships and accountability). Common examples of separation are production and test
workloads being run in separate accounts, or using a separate account so that the invoice and
billing data can be provided to the individual business units or departments in the organization
or stakeholder who owns the account.
• Define grouping requirements: Requirements for grouping do not override the separation
requirements, but are used to assist management. Group together similar environments or
workloads that do not require separation. An example of this is grouping multiple test or
development environments from one or more workloads together.
• Define account structure: Using these separations and groupings, specify an account for
each group and maintain separation requirements. These accounts are your member or linked
accounts. By grouping these member accounts under a single management or payer account, you
combine usage, which allows for greater volume discounts across all accounts, which provides
a single bill for all accounts. It's possible to separate billing data and provide each member
account with an individual view of their billing data. If a member account must not have its
usage or billing data visible to any other account, or if a separate bill from AWS is required,
define multiple management or payer accounts. In this case, each member account has its own
management or payer account. Resources should always be placed in member or linked accounts.
The management or payer accounts should only be used for management.
