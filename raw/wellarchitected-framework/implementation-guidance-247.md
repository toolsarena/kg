---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 878
---

# Implementation guidance

Consider the time savings that will allow your team to focus on retiring technical debt, innovation,
value-adding features and building what differentiates the business. For example, you might need
to lift and shift (also known as rehost) your databases from your on-premises environment to the
cloud as rapidly as possible and optimize later. It is worth exploring the possible savings attained
by using managed services on AWS that may remove or reduce license costs. Managed services on
AWS remove the operational and administrative burden of maintaining a service, such as patching
or upgrading the OS, and allow you to focus on innovation and business.
Since managed services operate at cloud scale, they can offer a lower cost per transaction or
service. You can make potential optimizations in order to achieve some tangible benefit, without
changing the core architecture of the application. For example, you may be looking to reduce the
amount of time you spend managing database instances by migrating to a database-as-a-service
platform like Amazon Relational Database Service (Amazon RDS) or migrating your application to a
fully managed platform like AWS Elastic Beanstalk.
Usually, managed services have attributes that you can set to ensure sufficient capacity. You
must set and monitor these attributes so that your excess capacity is kept to a minimum and
performance is maximized. You can modify the attributes of AWS Managed Services using the
AWS Management Console or AWS APIs and SDKs to align resource needs with changing demand.
For example, you can increase or decrease the number of nodes on an Amazon EMR cluster (or an
Amazon Redshift cluster) to scale out or in.
You can also pack multiple instances on an AWS resource to activate higher density usage. For
example, you can provision multiple small databases on a single Amazon Relational Database
Service (Amazon RDS) database instance. As usage grows, you can migrate one of the databases to
a dedicated Amazon RDS database instance using a snapshot and restore process.
When provisioning workloads on managed services, you must understand the requirements of
adjusting the service capacity. These requirements are typically time, effort, and any impact to
normal workload operation. The provisioned resource must allow time for any changes to occur,
provision the required overhead to allow this. The ongoing effort required to modify services
can be reduced to virtually zero by using APIs and SDKs that are integrated with system and
monitoring tools, such as Amazon CloudWatch.
Amazon RDS, Amazon Redshift, and Amazon ElastiCache provide a managed database service.
Amazon Athena, Amazon EMR, and Amazon OpenSearch Service provide a managed analytics
service.
