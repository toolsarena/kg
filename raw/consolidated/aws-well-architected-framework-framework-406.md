---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 535
---

# AWS Well-Architected Framework Framework

Design your API and workload components to be idempotent. Incorporate idempotency checks
into your workload components. Before you process a request or perform an operation, check
if the unique identifier has already been processed. If it has, return the previous result instead
of executing the operation again. For example, if a client sends a request to create a user, check
if a user with the same unique identifier already exists. If the user exists, it should return the
existing user information instead of creating a new one. Similarly, if a queue consumer receives a
message with a duplicate idempotency token, the consumer should ignore the message.
Create comprehensive test suites that validate the idempotency of requests. They should cover a
wide range of scenarios, such as successful requests, failed requests, and duplicate requests.
If your workload leverages AWS Lambda functions, consider Powertools for AWS Lambda.
Powertools for AWS Lambda is a developer toolkit that helps implement serverless best
practices and increase developer velocity when you work with AWS Lambda functions. In
particular, it provides a utility to convert your Lambda functions into idempotent operations
which are safe to retry.
