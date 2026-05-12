---
title: "SEC01-BP02 Secure account root user and properties"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 270
---

# SEC01-BP02 Secure account root user and properties

The root user is the most privileged user in an AWS account, with full administrative access to
all resources within the account, and in some cases cannot be constrained by security policies.
Deactivating programmatic access to the root user, establishing appropriate controls for the root
user, and avoiding routine use of the root user helps reduce the risk of inadvertent exposure of the
root credentials and subsequent compromise of the cloud environment.
Desired outcome: Securing the root user helps reduce the chance that accidental or intentional
damage can occur through the misuse of root user credentials. Establishing detective controls can
also alert the appropriate personnel when actions are taken using the root user.
