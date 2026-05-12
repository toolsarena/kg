---
title: "Questions"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 290
---

# Questions

• SEC 2. How do you manage authentication for people and machines?
• SEC 3. How do you manage permissions for people and machines?
SEC 2. How do you manage authentication for people and machines?
There are two types of identities you need to manage when approaching operating secure AWS
workloads.
• Human identities: The human identities that require access to your AWS environments and
applications can be categorized into three groups: workforce, third parties, and users.
The workforce group includes administrators, developers, and operators who are members of
your organization. They need access to manage, build, and operate your AWS resources.
Third parties are external collaborators, such as contractors, vendors, or partners. They interact
with your AWS resources as part of their engagement with your organization.
Users are the consumers of your applications. They access your AWS resources through web
browsers, client applications, mobile apps, or interactive command-line tools.
• Machine identities: Your workload applications, operational tools, and components require an
identity to make requests to AWS services, such as reading data. These identities also include


# Questions

• COST 5. How do you evaluate cost when you select services?