---
title: "SEC02-BP06 Employ user groups and attributes"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 310
---

# SEC02-BP06 Employ user groups and attributes

Defining permissions according to user groups and attributes helps reduce the number and
complexity of policies, making it simpler to achieve the principle of least privilege. You can use
user groups to manage the permissions for many people in one place based on the function they
perform in your organization. Attributes, such as department, project, or location, can provide
an additional layer of permission scope when people perform a similar function but for different
subsets of resources.
Desired outcome: You can apply changes in permissions based on function to all users who
perform that function. Group membership and attributes govern user permissions, reducing the
need to manage permissions at the individual user level. The groups and attributes you define in
your identity provider (IdP) are propagated automatically to your AWS environments.
