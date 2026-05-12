---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 361
---

# Implementation steps

1. Analyze and prioritize alerts.
a. Consolidate security alerts from various AWS services into Security Hub CSPM for centralized
visibility, prioritization, and remediation.
2. Develop remediations.
a. Use services such as Systems Manager and AWS Lambda to run programmatic remediations.
3. Configure how remediations are initiated.
a. Using Systems Manager, define custom actions that publish findings to EventBridge.
Configure these actions to be initiated manually or automatically.
