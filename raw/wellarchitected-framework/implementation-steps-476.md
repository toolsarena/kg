---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 942
---

# Implementation steps

• Conduct an inventory: Conduct a comprehensive inventory to identify all assets within your
workload.
• Analyze usage: Use continuous monitoring to identify static assets that are no longer required.
• Remove unused assets: Develop a plan to remove assets that are no longer required.
• Before removing any asset, evaluate the impact of removing it on the architecture.
• Consolidate overlapping generated assets to remove redundant processing.
• Update your applications to no longer produce and store assets that are not required.
• Communicate with third parties: Instruct third parties to stop producing and storing assets
managed on your behalf that are no longer required. Ask to consolidate redundant assets.
• Use lifecycle policies: Use lifecycle policies to automatically delete unused assets.
• You can use Amazon S3 Lifecycle to manage your objects throughout their lifecycle.
• You can use Amazon Data Lifecycle Manager to automate the creation, retention, and deletion
of Amazon EBS snapshots and Amazon EBS-backed AMIs.
• Review and optimize: Regularly review your workload to identify and remove any unused assets.
