---
title: "6. Implement canary deployments:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 463
---

# 6. Implement canary deployments:

• Configure your deployment process to support canary deployments, where changes are
rolled out to a subset of instances or users before you deploy them to the entire production
environment.
• Use services like AWS CodeDeploy or AWS ECS to manage canary deployments and monitor
the impact of changes.
• Implement rollback mechanisms to revert to the previous stable version if issues are detected
during the canary deployment.
