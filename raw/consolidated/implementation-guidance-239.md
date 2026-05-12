---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 860
---

# Implementation guidance

To establish strong accountability, consider your account strategy first as part of your cost
allocation strategy. Get this right, and you may not need to go any further. Otherwise, there can be
unawareness and further pain points.
To encourage accountability of cloud spend, grant users access to tools that provide visibility
into their costs and usage. AWS recommends that you configure all workloads and teams for the
following purposes:
• Organize: Establish your cost allocation and governance baseline with your own tagging strategy
and taxonomy. Create multiple AWS Accounts with tools such as AWS Control Tower or AWS
Organization. Tag the supported AWS resources and categorize them meaningfully based on
your organization structure (business units, departments, or projects). Tag account names for
specific cost centers and map them with AWS Cost Categories to group accounts for business
units to their cost centers so that business unit owner can see multiple accounts' consumption in
one place.
• Access: Track organization-wide billing information in consolidated billing. Verify the right
stakeholders and business owners have access.
• Control: Build effective governance mechanisms with the right guardrails to prevent unexpected
scenarios when using Service Control Policies (SCP), tag policies, IAM policies and budget alerts.
For example, you can allow teams to create specific resources in preferred regions only by using
effective control mechanisms and prevent resource creations without specific tag (such as cost-
center).
• Current state: Configure a dashboard that shows current levels of cost and usage. The dashboard
should be available in a highly visible place within the work environment like an operations
