---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 555
---

# Implementation steps

• Identify and understand the stateful components in your application.
• Decouple data by separating and managing user data from the core application logic.
• Amazon Cognito can decouple user data from application code by using features, such as
identity pools, user pools, and Amazon Cognito Sync.
• You can use AWS Secrets Manager decouple user data by storing secrets in a secure,
centralized location. This means that the application code doesn't need to store secrets, which
makes it more secure.
• Consider using Amazon S3 to store large, unstructured data, such as images and documents.
Your application can retrieve this data when required, eliminating the need to store it in
memory.
• Use Amazon DynamoDB to store information such as user profiles. Your application can query
this data in near-real time.
• Offload session data to a database, cache, or external files.
• Amazon ElastiCache, Amazon DynamoDB, Amazon Elastic File System (Amazon EFS), and
Amazon MemoryDB are examples of AWS services that you can use to offload session data.
