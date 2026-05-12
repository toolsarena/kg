---
title: "Operational guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 273
---

# Operational guidance

• Determine who in the organization should have access to the root user credentials.
• Use a two-person rule so that no one individual has access to all necessary credentials and MFA
to obtain root user access.
• Verify that the organization, and not a single individual, maintains control over the phone
number and email alias associated with the account (which are used for password reset and
MFA reset flow).
• Use root user only by exception (CIS 1.7).
• The AWS root user must not be used for everyday tasks, even administrative ones. Only log
in as the root user to perform AWS tasks that require root user. All other actions should be
performed by other users assuming appropriate roles.
• Periodically check that access to the root user is functioning so that procedures are tested prior
to an emergency situation requiring the use of the root user credentials.
• Periodically check that the email address associated with the account and those listed under
Alternate Contacts work. Monitor these email inboxes for security notifications you might receive
from <abuse@amazon.com>. Also ensure any phone numbers associated with the account are
working.
• Prepare incident response procedures to respond to root account misuse. Refer to the AWS
Security Incident Response Guide and the best practices in the Incident Response section of the
