---
title: "SEC03-BP09 Share resources securely with a third party"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 344
---

# SEC03-BP09 Share resources securely with a third party

The security of your cloud environment doesn't stop at your organization. Your organization might
rely on a third party to manage a portion of your data. The permission management for the third-
party managed system should follow the practice of just-in-time access using the principle of least
privilege with temporary credentials. By working closely with a third party, you can reduce the
scope of impact and risk of unintended access together.
Desired outcome: You avoid using long-term AWS Identity and Access Management (IAM)
credentials like access keys and secret keys, as they pose a security risk if misused. Instead, you
use IAM roles and temporary credentials to improve your security posture and minimize the
operational overhead of managing long-term credentials. When granting third-party access,
you use a universally unique identifier (UUID) as the external ID in the IAM trust policy and keep
the IAM policies attached to the role under your control to ensure least privilege access. For
prescriptive guidance on analyzing externally shared resources, see SEC03-BP07 Analyze public and
cross-account access.
