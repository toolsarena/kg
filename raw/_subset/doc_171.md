---
title: "AWS Elastic Disaster Recovery"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 692
---

# AWS Elastic Disaster Recovery

If you are considering the pilot light or warm standby strategy for disaster recovery, AWS Elastic
Disaster Recovery could provide an alternative approach with improved benefits. Elastic Disaster
Recovery can offer an RPO and RTO target similar to warm standby, but maintain the low-cost
approach of pilot light. Elastic Disaster Recovery replicates your data from your primary region
to your recovery Region, using continual data protection to achieve an RPO measured in seconds
and an RTO that can be measured in minutes. Only the resources required to replicate the data
are deployed in the recovery region, which keeps costs down, similar to the pilot light strategy.
When using Elastic Disaster Recovery, the service coordinates and orchestrates the recovery of
compute resources when initiated as part of failover or drill.


# AWS Glossary

For the latest AWS terminology, see the AWS glossary in the AWS Glossary Reference.

# AWS Glossary

For the latest AWS terminology, see the AWS glossary in the AWS Glossary Reference.

# AWS Glue time-based schedule Define a time-based schedule for your

crawlers and jobs in AWS Glue.

# AWS Glue time-based schedule Define a time-based schedule for your

crawlers and jobs in AWS Glue.

# AWS IoT Greengrass Run local compute, messaging, and data

caching for connected devices.

# AWS IoT Greengrass Run local compute, messaging, and data

caching for connected devices.