---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 339
---

# AWS Well-Architected Framework Framework

• Configure AWS Identity and Access Management Access Analyzer: IAM Access Analyzer helps
you identify resources in your organization and accounts, such as Amazon S3 buckets or IAM
roles that are shared with an external entity.
• Use auto-remediation in AWS Config to respond to changes in public access configuration of
Amazon S3 buckets: You can automatically turn on the block public access settings for Amazon
S3 buckets.
• Implement monitoring and alerting to identify if Amazon S3 buckets have become public:
You must have monitoring and alerting in place to identify when Amazon S3 Block Public
Access is turned off, and if Amazon S3 buckets become public. Additionally, if you are using
AWS Organizations, you can create a service control policy that prevents changes to Amazon
S3 public access policies. AWS Trusted Advisor checks for Amazon S3 buckets that have open
access permissions. Bucket permissions that grant, upload, or delete access to everyone create
potential security issues by allowing anyone to add, modify, or remove items in a bucket. The
Trusted Advisor check examines explicit bucket permissions and associated bucket policies that
might override the bucket permissions. You also can use AWS Config to monitor your Amazon S3
buckets for public access. For more information, see How to Use AWS Config to Monitor for and
Respond to Amazon S3 Buckets Allowing Public Access.
When reviewing access controls for Amazon S3 buckets, it is important to consider the nature of
the data stored within them. Amazon Macie is a service designed to help you discover and protect
sensitive data, such as Personally Identifiable Information (PII), Protected Health Information (PHI),
and credentials like private keys or AWS access keys.


# AWS Well-Architected Framework Framework

• Make your AMI publicly available for use in Amazon EC2