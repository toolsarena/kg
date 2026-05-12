---
title: "You can create data exports with the following customizations:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 852
---

# You can create data exports with the following customizations:

• Include resource IDs
• Split cost allocation data
• Hourly granularity
• Versioning
• Compression type and file format
For your workloads that run containers on Amazon ECS or Amazon EKS, enable split cost allocation
data so that you can allocate your container costs to individual business units and teams, based
on how your container workloads consume shared compute and memory resources. Split cost
allocation data introduces cost and usage data for new container-level resources to AWS Cost
and Usage Report. Split cost allocation data is calculated by computing the cost of individual ECS
services and tasks running on the cluster.
A cost and usage dashboard exports the cost and usage dashboard table to an S3 bucket on
a recurring basis and deploys a prebuilt cost and usage dashboard to Quick. Use this option
if you want to quickly deploy a dashboard of your cost and usage data without the ability for
customization.
If desired, you can still export CUR in legacy mode, where you can integrate other processing
services such as AWS Glue to prepare the data for analysis and perform data analysis with Amazon
Athena using SQL to query the data.


# Zone (AZ) configurations

Level of risk exposed if this best practice is not established: Medium

# Zone (AZ) configurations

Level of risk exposed if this best practice is not established: Medium