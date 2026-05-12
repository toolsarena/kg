---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 331
---

# AWS Well-Architected Framework Framework

• Consider logging data events in AWS CloudTrail: By default, CloudTrail does not log data
events such as Amazon S3 object-level activity (for example, GetObject and DeleteObject)
or Amazon DynamoDB table activities (for example, PutItem and DeleteItem). Consider using
logging for these events to determine what users and roles need access to specific Amazon S3
objects or DynamoDB table items.
