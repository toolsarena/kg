---
title: "SEC02-BP04 Rely on a centralized identity provider"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 304
---

# SEC02-BP04 Rely on a centralized identity provider

For workforce identities (employees and contractors), rely on an identity provider that allows you
to manage identities in a centralized place. This makes it easier to manage access across multiple
applications and systems, because you are creating, assigning, managing, revoking, and auditing
access from a single location.
Desired outcome: You have a centralized identity provider where you centrally manage
workforce users, authentication policies (such as requiring multi-factor authentication (MFA)),
and authorization to systems and applications (such as assigning access based on a user's group
membership or attributes). Your workforce users sign in to the central identity provider and
federate (single sign-on) to internal and external applications, removing the need for users to
remember multiple credentials. Your identity provider is integrated with your human resources
(HR) systems so that personnel changes are automatically synchronized to your identity provider.
For example, if someone leaves your organization, you can automatically revoke access to
federated applications and systems (including AWS). You have enabled detailed audit logging in
your identity provider and are monitoring these logs for unusual user behavior.
