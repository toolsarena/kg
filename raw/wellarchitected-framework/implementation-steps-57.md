---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 330
---

# Implementation steps

• Use AWS Identity and Access Management Access Analyzer: IAM Access Analyzer helps identify
resources in your organization and accounts, such as Amazon Simple Storage Service (Amazon
S3) buckets or IAM roles that are shared with an external entity.
• Use IAM Access Analyzer policy generation: IAM Access Analyzer policy generation helps you
create fine-grained permission policies based on an IAM user or role’s access activity.
• Test permissions across lower environments before production: Start by using the less
critical sandbox and development environments to test the permissions required for various job
functions using IAM Access Analyzer. Then, progressively tighten and validate these permissions
across the testing, quality assurance, and staging environments before applying them to
production. The lower environments can have more relaxed permissions initially, as service
control policies (SCPs) enforce guardrails by limiting the maximum permissions granted.
• Determine an acceptable timeframe and usage policy for IAM users and roles: Use the
last accessed timestamp to identify unused users and roles and remove them. Review service
and action last accessed information to identify and scope permissions for specific users and
roles. For example, you can use last accessed information to identify the specific Amazon
S3 actions that your application role requires and restrict the role’s access to only those
actions. Last accessed information features are available in the AWS Management Console
and programmatically allow you to incorporate them into your infrastructure workflows and
automated tools.
