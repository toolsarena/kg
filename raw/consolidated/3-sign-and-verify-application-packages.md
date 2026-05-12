---
title: "3. Sign and verify application packages:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 463
---

# 3. Sign and verify application packages:

• Use AWS Signer or AWS Key Management Service (AWS KMS) to sign your application
packages after they have been tested and validated.
• Configure the deployment process to verify the signatures of the application packages before
you deploy them to the target environments.


# 3. Track and manage state

Maintain the state of each operation or request in your workload. This can be achieved by
storing the idempotency token and the corresponding state (such as pending, completed, or

# 3. Track and manage state

Maintain the state of each operation or request in your workload. This can be achieved by
storing the idempotency token and the corresponding state (such as pending, completed, or