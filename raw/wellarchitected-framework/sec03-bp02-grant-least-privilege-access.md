---
title: "SEC03-BP02 Grant least privilege access"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 318
---

# SEC03-BP02 Grant least privilege access

Grant only the access that users require to perform specific actions on specific resources under
specific conditions. Use group and identity attributes to dynamically set permissions at scale, rather
than defining permissions for individual users. For example, you can allow a group of developers
access to manage only resources for their project. This way, if a developer leaves the project, their
access is automatically revoked without changing the underlying access policies.
Desired outcome: Users have only the minimum permissions required for their specific job
functions. You use separate AWS accounts to isolate developers from production environments.
When developers need to access production environments for specific tasks, they are granted
limited and controlled access only for the duration of those tasks. Their production access is
immediately revoked after they complete the necessary work. You conduct regular reviews of
permissions and promptly revoke them when no longer needed, such as when a user changes roles
or leaves the organization. You restrict administrator privileges to a small, trusted group to reduce
risk exposure. You give machine or system accounts only the minimum permissions required to
perform their intended tasks.
