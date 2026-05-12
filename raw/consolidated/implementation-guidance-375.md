---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 311
---

# Implementation guidance

AWS permissions are defined in documents called policies that are associated with a principal,
such as a user, group, role, or resource. You can scale permissions management by organizing
permissions assignments (group, permissions, account) based on job-function, workload, and
SDLC environment. For your workforce, this allows you to define groups based on the function
your users perform for your organization, rather than based on the resources being accessed.
For example, a WebAppDeveloper group may have a policy attached for configuring services like
Amazon CloudFront within a development account. An AutomationDeveloper group may have
some overlapping permissions with the WebAppDeveloper group. These common permissions can
be captured in a separate policy and associated with both groups, rather than having users from
both functions belong to a CloudFrontAccess group.
In addition to groups, you can use attributes to further scope access. For example, you may have a
Project attribute for users in your WebAppDeveloper group to scope access to resources specific
to their project. Using this technique removes the need to have different groups for application
developers working on different projects if their permissions are otherwise the same. The way
you refer to attributes in permission policies is based on their source, whether they are defined as
part of your federation protocol (such as SAML, OIDC, or SCIM), as custom SAML assertions, or set
within IAM Identity Center.
