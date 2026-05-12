---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 304
---

# Common anti-patterns:

• You do not use federation and single-sign on. Your workforce users create separate user accounts
and credentials in multiple applications and systems.
• You have not automated the lifecycle of identities for workforce users, such as by integrating
your identity provider with your HR systems. When a user leaves your organization or changes
roles, you follow a manual process to delete or update their records in multiple applications and
systems.
Benefits of establishing this best practice: By using a centralized identity provider, you have
a single place to manage workforce user identities and policies, the ability to assign access to
applications to users and groups, and the ability to monitor user sign-in activity. By integrating


# Common anti-patterns:

• Not auditing credential use.
• Using long-term credentials unnecessarily.
• Using long-term credentials and not rotating them regularly.
Level of risk exposed if this best practice is not established: High