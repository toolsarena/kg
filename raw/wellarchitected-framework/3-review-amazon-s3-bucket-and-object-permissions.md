---
title: "3. Review Amazon S3 bucket and object permissions:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 410
---

# 3. Review Amazon S3 bucket and object permissions:

• Regularly review the level of access granted in Amazon S3 bucket policies.
• Avoid using publicly readable or writeable buckets unless absolutely necessary.
• Consider using AWS Config to detect publicly available buckets.
• Use Amazon CloudFront to serve content from Amazon S3.
• Verify that buckets that should not allow public access are properly configured to prevent it.
• You can apply the same review process for databases and any other data sources that use IAM
authentication, such as SQS or third-party data stores.
