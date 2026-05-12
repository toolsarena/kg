---
title: "3. Establish logging and audit trails:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 414
---

# 3. Establish logging and audit trails:

• Enable CloudTrail logs to track access to the accounts holding certificate authorities. Consider
configuring log file integrity validation in CloudTrail to verify the authenticity of the log data.
• Periodically generate and review audit reports that list the certificates that your private CA has
issued or revoked. These reports can be exported to an S3 bucket.
• When deploying a private CA, you will also need to establish an S3 bucket to store the
Certificate Revocation List (CRL). For guidance on configuring this S3 bucket based on your
workload's requirements, see Planning a certificate revocation list (CRL).


# 3. For out-of-band inspection solutions:

1. Turn on VPC Traffic Mirroring on interfaces where inbound and outbound traffic should be
mirrored. You can use Amazon EventBridge rules to invoke an AWS Lambda function to turn

# 3. For out-of-band inspection solutions:

1. Turn on VPC Traffic Mirroring on interfaces where inbound and outbound traffic should be
mirrored. You can use Amazon EventBridge rules to invoke an AWS Lambda function to turn