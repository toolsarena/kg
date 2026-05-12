---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 872
---

# Implementation steps

• Use Amazon Data Lifecycle Manager: Use lifecycle policies on Amazon Data Lifecycle Manager
to automate deletion of Amazon EBS snapshots and Amazon EBS-backed AMIs.
• Set up lifecycle configuration on a bucket: Use Amazon S3 lifecycle configuration on a bucket
to define actions for Amazon S3 to take during an object's lifecycle, as well as deletion at the end
of the object's lifecycle, based on your business requirements.
