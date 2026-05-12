---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 269
---

# AWS Well-Architected Framework Framework

Tower. Review the list of highly recommended and optional controls, and implement controls
that are appropriate to your needs.
4. Restrict access to newly added Regions: For new AWS Regions, IAM resources such as users
and roles are only propagated to the Regions that you specify. This action can be performed
through the console when using Control Tower, or by adjusting IAM permission policies in AWS
Organizations.
5. Consider AWS CloudFormation StackSets: StackSets help you deploy resources including IAM
policies, roles, and groups into different AWS accounts and Regions from an approved template.
