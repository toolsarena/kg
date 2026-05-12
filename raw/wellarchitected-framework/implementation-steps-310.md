---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 336
---

# Implementation steps

1. Define and document an access management lifecycle process, including procedures for granting
initial access, periodic reviews, and offboarding.
2. Implement IAM roles, groups, and permissions boundaries to manage access collectively and
enforce maximum permissible access levels.
3. Integrate with a federated identity provider (such as Microsoft Active Directory, Okta, Ping
Identity) as the authoritative source for user and group information using IAM Identity Center.
4. Use the SCIM protocol to synchronize user and group information from the identity provider into
IAM Identity Center's Identity Store.
