---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 855
---

# AWS Well-Architected Framework Framework

• Define a tagging schema: Gather all stakeholders from across your business to define a schema.
This typically includes people in technical, financial, and management roles. Define a list of tags
that all resources must have, as well as a list of tags that resources should have. Verify that the
tag names and values are consistent across your organization.
• Tag resources: Using your defined cost attribution categories, place tags on all resources in your
workloads according to the categories. Use tools such as the CLI, Tag Editor, or AWS Systems
Manager to increase efficiency.
• Implement AWS Cost Categories: You can create Cost Categories without implementing
tagging. Cost categories use the existing cost and usage dimensions. Create category rules from
your schema and implement them into cost categories.
• Automate tagging: To verify that you maintain high levels of tagging across all resources,
automate tagging so that resources are automatically tagged when they are created. Use services
such as AWS CloudFormation to verify that resources are tagged when created. You can also
create a custom solution to tag automatically using Lambda functions or use a microservice that
scans the workload periodically and removes any resources that are not tagged, which is ideal for
test and development environments.
• Monitor and report on tagging: To verify that you maintain high levels of tagging across your
organization, report and monitor the tags across your workloads. You can use AWS Cost Explorer
to view the cost of tagged and untagged resources, or use services such as Tag Editor. Regularly
review the number of untagged resources and take action to add tags until you reach the desired
level of tagging.


# AWS Well-Architected Framework Framework

• You can involve the right owners when troubleshooting issues.
Level of risk exposed if this best practice is not established: High

# AWS Well-Architected Framework Framework

• How can I tag my AWS resources to divide up my bill by cost center or project
• Tagging AWS Resources