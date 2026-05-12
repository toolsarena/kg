---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 931
---

# Implementation steps

• Build once and deploy many: Use infrastructure-as-code such as CloudFormation, AWS SDK, or
AWS CLI to deploy once and use many times for similar environments or for disaster recovery
scenarios. Tag while deploying to track your consumption as defined in other best practices.
Use AWS Launch Wizard to reduce the time to deploy many popular enterprise workloads. AWS
Launch Wizard guides you through the sizing, configuration, and deployment of enterprise
workloads following AWS best practices. You can also use the Service Catalog, which helps you
create and manage infrastructure-as-code approved templates for use on AWS so anyone can
discover approved, self-service cloud resources.
• Automate continuous compliance: Consider automating assessment and remediation of
recorded configurations against predefined standards. When you combine AWS Organizations
