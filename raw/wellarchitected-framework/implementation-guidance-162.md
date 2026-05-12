---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 596
---

# Implementation guidance

The most common resiliency testing forms that can be integrated in your system's deployments are
disaster recovery and chaos engineering.
• Include updates to your disaster recovery plans and standard operating procedures (SOPs) with
any significant deployment.
• Integrate reliability testing into your automated deployment pipelines. Services such asAWS
Resilience Hubcan be integrated into your CI/CD pipeline to establish continuous resilience
assessments that are automatically evaluated as part of every deployment.
• Define your applications in AWS Resilience Hub. Resilience assessments generate code snippets
that help you create recovery procedures as AWS Systems Manager documents for your
applications and provide a list of recommended Amazon CloudWatch monitors and alarms.
