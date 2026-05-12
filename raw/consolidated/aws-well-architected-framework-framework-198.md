---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 268
---

# AWS Well-Architected Framework Framework

allowing you to filter permissions available to member accounts located at lower levels of an OU
hierarchy. A good design takes advantage of this inheritance to reduce the number and complexity
of security policies required to achieve the desired security controls for each member account.
AWS Organizations and AWS Control Tower are two services that you can use to implement and
manage this multi-account structure in your AWS environment. AWS Organizations allows you to
organize accounts into a hierarchy defined by one or more layers of OUs, with each OU containing
a number of member accounts. Service control policies (SCPs) allow the organization administrator
to establish granular preventative controls on member accounts, and AWS Config can be used to
establish proactive and detective controls on member accounts. Many AWS services integrate with
