---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 645
---

# AWS Well-Architected Framework Framework

are not included in the SLA. There could be rare events in which the data plane’s resilient design
allows it to maintain availability while the control planes do not. For disaster recovery and failover
mechanisms, use data plane functions to provide the best possible reliability.
Design your compute infrastructure to be statically stable to avoid using the control plane during
an incident. For example, if you are using Amazon EC2 instances, avoid provisioning new instances
manually or instructing Auto Scaling Groups to add instances in response. For the highest levels
of resilience, provision sufficient capacity in the cluster used for failover. If this capacity threshold
must be limited, set throttles on the overall end-to-end system to safely limit the total traffic
reaching the limited set of resources.
For services like Amazon DynamoDB, Amazon API Gateway, load balancers, and AWS Lambda
serverless, using those services leverages the data plane. However, creating new functions, load
balancers, API gateways, or DynamoDB tables is a control plane action and should be completed
before the degradation as preparation for an event and rehearsal of failover actions. For Amazon
RDS, data plane actions allow for access to data.
For more information about data planes, control planes, and how AWS builds services to meet high
availability targets, see Static stability using Availability Zones.
Understand which operations are on the data plane and which are on the control plane.
