---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 332
---

# Common anti-patterns:

• Creating member AWS accounts within an AWS Organization, but not using SCPs to restrict the
use and permissions available to their root credentials.
• Assigning permissions based on least privilege, but not placing guardrails on the maximum set of
permissions that can be granted.
• Relying on the implicit deny foundation of AWS IAM to restrict permissions, trusting that policies
will not grant an undesired explicit allow permission.
• Running multiple workload environments in the same AWS account, and then relying on
mechanisms such as VPCs, tags, or resource policies to enforce permission boundaries.
Benefits of establishing this best practice: Permission guardrails help build confidence that
undesired permissions cannot be granted, even when a permission policy attempts to do so. This
can simplify defining and managing permissions by reducing the maximum scope of permissions
needing consideration.
Level of risk exposed if this best practice is not established: Medium
