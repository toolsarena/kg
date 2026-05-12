---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 340
---

# Common anti-patterns:

• Lack of process to continually monitor and automatically alert on unexpected external share.
• Lack of baseline on what should be shared and what should not.
• Defaulting to a broadly open policy rather than sharing explicitly when required.
• Manually creating foundational resources that overlap when required.
Level of risk exposed if this best practice is not established: Medium


# Common anti-patterns:

• Using the default IAM trust policy without any conditions.
• Using long-term IAM credentials and access keys.
• Reusing external IDs.
Level of risk exposed if this best practice is not established: Medium

# Common anti-patterns:

• Logs are stored in perpetuity or deleted too soon.
• Everybody can access logs.
• Relying entirely on manual processes for log governance and use.
• Storing every single type of log just in case it is needed.
• Checking log integrity only when necessary.