---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 94
---

# Implementation steps

1. Start by defining ownership for your organization. Ownership can imply who owns the risk
for the resource, who owns changes to the resource, or who supports the resource when
troubleshooting. Ownership could also imply financial or administrative ownership of the
resource.
2. Use AWS Organizations to manage accounts. You can manage the alternate contacts for your
accounts centrally.
a. Using company owned email addresses and phone numbers for contact information helps
you to access them even if the individuals whom they belong to are no longer with your
organization. For example, create separate email distribution lists for billing, operations,
and security and configure these as Billing, Security, and Operations contacts in each active
AWS account. Multiple people will receive AWS notifications and be able to respond, even if
someone is on vacation, changes roles, or leaves the company.
b. If an account is not managed by AWS Organizations, alternate account contacts help AWS
get in contact with the appropriate personnel if needed. Configure the account's alternate
contacts to point to a group rather than an individual.
3. Use tags to identify owners for AWS resources. You can specify both owners and their contact
information in separate tags.
