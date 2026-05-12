---
title: "Additional steps when using multiple AWS Regions"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 625
---

# Additional steps when using multiple AWS Regions

1. Replicate all operating system (OS) and application code used by your workload across your
selected Regions. Replicate Amazon Machine Images (AMIs) used by your EC2 instances if
necessary using solutions such as Amazon EC2 Image Builder. Replicate container images stored
in registries using solutions such as Amazon ECR cross-Region replication. Enable Regional
replication for any Amazon S3 buckets used for storing application resources.
2. Deploy your compute resources and configuration metadata (such as parameters stored in AWS
Systems Manager Parameter Store) into multiple Regions. Use the same procedures described in
previous steps, but replicate the configuration for each Region you are using for your workload.
Use infrastructure as code solutions such as AWS CloudFormation to uniformly reproduce the
configurations among Regions. If you are using a secondary Region in a pilot light configuration
for disaster recovery, you may reduce the number of your compute resources to a minimum
value to save cost, with a corresponding increase in time to recovery.
3. Replicate your data from your primary Region into your secondary Regions.
a. Amazon DynamoDB global tables provide global replicas of your data that can be written to
from any supported Region. With other AWS-managed data services, such as Amazon RDS,
Amazon Aurora, and Amazon Elasticache, you designate a primary (read/write) Region and
replica (read-only) Regions. Consult the respective services' user and developer guides for
details on Regional replication.
b. If you are running a self-managed database, arrange for multi-Region replication according
to the application's instructions or best practices. Familiarize yourself with the failover
procedures for your application.
c. If your workload uses AWS EventBridge, you may need to forward selected events from your
primary Region to your secondary Regions. To do so, specify event buses in your secondary
Regions as targets for matched events in your primary Region.
4. Consider whether and to what extent you want to use identical encryption keys across Regions.
A typical approach that balances security and ease of use is to use Region-scoped keys for
Region-local data and authentication, and use globally-scoped keys for encryption of data that
is replicated among different Regions. AWS Key Management Service (KMS) supports multi-
region keys to securely distribute and protect keys shared across Regions.
5. Consider AWS Global Accelerator to improve the availability of your application by directing
traffic to Regions that contain healthy endpoints.


# AI

• Use the latest high performant libraries and GPU drivers.
• Use automation to release GPU instances when not in use.

# AI

• Keep up to date: Use the latest high performant libraries and GPU drivers.
• Release unneeded instances: Use automation to release GPU instances when not in use.

# AI

• AWS Cloud Operations & Migrations Blog - Implementing automated and centralized tagging
controls with AWS Config and AWS Organizations

# AI

• Use the latest high performant libraries and GPU drivers.
• Use automation to release GPU instances when not in use.

# AI

• Keep up to date: Use the latest high performant libraries and GPU drivers.
• Release unneeded instances: Use automation to release GPU instances when not in use.

# AI

• AWS Cloud Operations & Migrations Blog - Implementing automated and centralized tagging
controls with AWS Config and AWS Organizations