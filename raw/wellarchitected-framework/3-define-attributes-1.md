---
title: "3. Define attributes:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 312
---

# 3. Define attributes:

a. If you use an external identity provider, both the SCIM and SAML 2.0 protocols provide certain
attributes by default. Additional attributes can be defined and passed using SAML assertions
with the https://aws.amazon.com/SAML/Attributes/PrincipalTag attribute name.
Refer to your identity provider's documentation for guidance on defining and configuring
custom attributes.
b. If you define roles within IAM Identity Center, enable the attribute-based access control
(ABAC) feature, and define attributes as desired. Consider attributes that align with your
organization's structure or resource tagging strategy.
If you require IAM role chaining from IAM Roles assumed through IAM Identity center, values like
source-identity and principal-tags will not propagate. For more detail, see Enable and
configure attributes for access control.
