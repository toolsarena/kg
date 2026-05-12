---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 328
---

# AWS Well-Architected Framework Framework

• Monitor the emergency access account for activity by creating EventBridge rules that match on
console login and API activity by the emergency IAM roles. Send notifications to your security
operations center when activity happens outside of an ongoing emergency event tracked in your
incident management system.
Additional steps for Failure Mode 1: Identity provider used to federate to AWS is unavailable
and Failure Mode 2: Identity provider configuration on AWS is modified or has expired
• Pre-create resources depending on the mechanism you choose for emergency access:
• Using IAM users: pre-create the IAM users with strong passwords and associated MFA devices.
• Using the emergency account root user: configure the root user with a strong password and
store the password in your enterprise credential vault. Associate multiple physical MFA devices
with the root user and store the devices in locations that can be accessed quickly by members
of your emergency administrator team.
