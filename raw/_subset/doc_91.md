---
title: "5. If you need credentials for the root user:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 272
---

# 5. If you need credentials for the root user:

a. Use a complex password.
b. Turn on multi-factor authentication (MFA) for the root user, especially for AWS Organizations
management (payer) accounts (CIS 1.5).
c. Consider hardware MFA devices for resiliency and security, as single use devices can reduce
the chances that the devices containing your MFA codes might be reused for other purposes.
Verify that hardware MFA devices powered by a battery are replaced regularly. (CIS 1.6)
• To configure MFA for the root user, follow the instructions for creating either a virtual
MFA or hardware MFA device.
d. Consider enrolling multiple MFA devices for backup. Up to 8 MFA devices are allowed per
account.
• Note that enrolling more than one MFA device for the root user automatically turns off
the flow for recovering your account if the MFA device is lost.
e. Store the password securely, and consider circular dependencies if storing the password
electronically. Don’t store the password in such a way that would require access to the same
AWS account to obtain it.
6. Optional: Consider establishing a periodic password rotation schedule for the root user.
