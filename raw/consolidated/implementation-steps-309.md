---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 334
---

# Implementation steps

1. Isolate your workloads and environments into separate AWS accounts.
2. Use SCPs to reduce the maximum set of permissions that can be granted to principals within the
member accounts of your organization.
a. When defining SCPs to reduce the maximum set of permissions that can be granted to
principals within your organization's member accounts, you can choose between an allow
list or deny list approach. The allow list strategy explicitly specifies the access that is allowed
and implicitly blocks all other access. The deny list strategy explicitly specifies the access that
isn't allowed and allows all other access by default. Both strategies have their advantages and
trade-offs, and the appropriate choice depends on your organization's specific requirements
and risk model. For more detail, see Strategy for using SCPs.
b. Additionally, review the service control policy examples to understand how to construct SCPs
effectively.
3. Use IAM resource policies to scope down and specify conditions for permitted actions on
resources. Use conditions in IAM role trust policies to create restrictions on assuming roles.
4. Assign IAM permission boundaries to IAM roles that workload teams can then use to manage
their own workload IAM roles and permissions.
5. Evaluate PAM and TEAM solutions based on your needs.
