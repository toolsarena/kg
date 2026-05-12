---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 845
---

# AWS Well-Architected Framework Framework

receive only the access necessary to complete their tasks. This minimizes the risk associated with
unauthorized access or misuse.
After you develop policies, you can create logical groups and user roles within your organization.
This allows you to assign permissions, control usage, and help implement robust access control
mechanisms, preventing unauthorized access to sensitive information. Begin with high-level
groupings of people. Typically, this aligns with organizational units and job roles (for example, a
systems administrator in the IT Department, financial controller, or business analysts). The groups
categorize people that do similar tasks and need similar access. Roles define what a group must
do. It is easier to manage permissions for groups and roles than for individual users. Roles and
groups assign permissions consistently and systematically across all users, preventing errors and
inconsistencies.
When a user’s role changes, administrators can adjust access at the role or group level, rather than
reconfiguring individual user accounts. For example, a systems administrator in IT requires access to
create all resources, but an analytics team member only needs to create analytics resources.
