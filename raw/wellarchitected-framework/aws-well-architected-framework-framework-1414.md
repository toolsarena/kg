---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 868
---

# AWS Well-Architected Framework Framework

• Delete your Auto Scaling infrastructure.
• Release all Dedicated Hosts.
• Delete all Amazon EBS volumes and Amazon EBS snapshots.
• Release all Elastic IP addresses.
• Deregister all Amazon Machine Images (AMIs).
• Terminate all AWS Elastic Beanstalk environments.
If the resource is an object in Amazon Glacier storage and if you delete an archive before meeting
the minimum storage duration, you will be charged a prorated early deletion fee. Amazon Glacier
minimum storage duration depends on the storage class used. For a summary of minimum
storage duration for each storage class, see Performance across the Amazon S3 storage classes.
For detail on how early deletion fees are calculated, see Amazon S3 pricing.
The following simple decommissioning process flowchart outlines the decommissioning steps.
Before decommissioning resources, verify that resources you have identified for decommissioning
are not being used by the organization.
Resource decommissioning flow.
