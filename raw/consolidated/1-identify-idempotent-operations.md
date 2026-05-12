---
title: "1. Identify idempotent operations"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 533
---

# 1. Identify idempotent operations

Determine which operations require idempotency. These typically include POST, PUT, and
DELETE HTTP methods and database insert, update, or delete operations. Operations that do
not mutate state, such as read-only queries, usually do not require idempotency unless they
have side effects.


# 1. Identify problems:

• Use data from previous incidents to identify recurring patterns that may indicate deeper
systemic issues.
• Leverage tools like AWS CloudTrail and Amazon CloudWatch to analyze trends and uncover
underlying problems.

# 1. Identify problems:

• Use data from previous incidents to identify recurring patterns that may indicate deeper
systemic issues.
• Leverage tools like AWS CloudTrail and Amazon CloudWatch to analyze trends and uncover
underlying problems.