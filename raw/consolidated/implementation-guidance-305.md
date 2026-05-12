---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 97
---

# Implementation guidance

• Processes and procedures have identified owners who are responsible for their definition.
• Identify the operations activities conducted in support of your workloads. Document these
activities in a discoverable location.
• Uniquely identify the individual or team responsible for the specification of an activity. They
are responsible to verify that it can be successfully performed by an adequately skilled team
member with the correct permissions, access, and tools. If there are issues with performing
that activity, the team members performing it are responsible for providing the detailed
feedback necessary for the activity to be improved.
• Capture ownership in the metadata of the activity artifact through services like AWS Systems
Manager, through documents, and AWS Lambda. Capture resource ownership using tags or
resource groups, specifying ownership and contact information. Use AWS Organizations to
create tagging polices and capture ownership and contact information.
• Over time, these procedures should be evolved to be runnable as code, reducing the need for
human intervention.
• For example, consider AWS Lambda functions, CloudFormation templates, or AWS Systems
Manager automation docs.
• Perform version control in appropriate repositories.
• Include suitable resource tagging so owners and documentation can readily be identified.
