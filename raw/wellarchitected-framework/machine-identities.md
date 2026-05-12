---
title: "Machine identities"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 296
---

# Machine identities

For machine identities, you might need to use long-term credentials. In these cases, you should
require workloads to use temporary credentials with IAM roles to access AWS.
• For Amazon Elastic Compute Cloud (Amazon EC2), you can use roles for Amazon EC2.
• AWS Lambda allows you to configure a Lambda execution role to grant the service permissions
to perform AWS actions using temporary credentials. There are many other similar models for
AWS services to grant temporary credentials using IAM roles.
• For IoT devices, you can use the AWS IoT Core credential provider to request temporary
credentials.
• For on-premises systems or systems that run outside of AWS that need access to AWS resources,
you can use IAM Roles Anywhere.
There are scenarios where temporary credentials are not supported, which require the use of long-
term credentials. In these situations, audit and rotate these credentials periodically and rotate
access keys regularly. For highly restricted IAM user access keys, consider the following additional
security measures:
• Grant highly restricted permissions:
• Adhere to the principle of least privilege (be specific about actions, resources, and conditions).
