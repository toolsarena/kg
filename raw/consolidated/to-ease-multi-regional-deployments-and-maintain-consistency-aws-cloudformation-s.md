---
title: "To ease multi-Regional deployments and maintain consistency, AWS CloudFormation StackSets"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 622
---

# To ease multi-Regional deployments and maintain consistency, AWS CloudFormation StackSets

can replicate your entire AWS infrastructure across multiple Regions. AWS CloudFormation can also
detect configuration drift and inform you when your AWS resources in a Region are out of sync.
Many AWS services offer multi-region replication for important workload assets. For example, EC2
Image Builder can publish your EC2 machine images (AMIs) after every build to each Region you
use. Amazon Elastic Container Registry (ECR) can replicate your container images to your selected
Regions.
You must also replicate your data across each of your chosen Regions. Many AWS managed data
services provide cross-Regional replication capability, including Amazon S3, Amazon DynamoDB,
Amazon RDS, Amazon Aurora, Amazon Redshift, Amazon Elasticache, and Amazon EFS. Amazon
DynamoDB global tables accept writes in any supported Region and will replicate data among
all your other configured Regions. With other services, you must designate a primary Region
for writes, as other Regions contain read-only replicas. For each AWS-managed data service
your workload uses, refer to its user guide and developer guide to understand its multi-Region
capabilities and limitations. Pay special attention to where writes must be directed, transactional
capabilities and limitations, how replication is performed, and how to monitor synchronization
between Regions.
AWS also provides the ability to route request traffic to your Regional deployments with great
flexibility. For example, you can configure your DNS records using Amazon Route 53 to direct traffic
to the closest available Region to the user. Alternatively, you can configure your DNS records in
an active/standby configuration, where you designate one Region as primary and fall back to a
Regional replica only if the primary Region becomes unhealthy. You can configure Route 53 health
checks to detect unhealthy endpoints and perform automatic failover and additionally use Amazon
