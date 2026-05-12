---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 696
---

# AWS Well-Architected Framework Framework

sources for more details. Rebuilding the infrastructure includes creating resources like EC2
instances in addition to the Amazon Virtual Private Cloud (Amazon VPC), subnets, and security
groups needed. You can automate much of the restoration process. To learn how, see this blog
post.
5. Determine and implement how you will reroute traffic to failover when needed (during a
disaster event).
This failover operation can be initiated either automatically or manually. Automatically initiated
failover based on health checks or alarms should be used with caution since an unnecessary
failover (false alarm) incurs costs such as non-availability and data loss. Manually initiated
failover is therefore often used. In this case, you should still automate the steps for failover, so
that the manual initiation is like the push of a button.
There are several traffic management options to consider when using AWS services. One option
is to use Amazon Route 53. Using Amazon Route 53, you can associate multiple IP endpoints
in one or more AWS Regions with a Route 53 domain name. To implement manually initiated
failover you can use Amazon Application Recovery Controller, which provides a highly available
data plane API to reroute traffic to the recovery Region. When implementing failover, use data
plane operations and avoid control plane ones as described in REL11-BP04 Rely on the data
plane and not the control plane during recovery.
To learn more about this and other options see this section of the Disaster Recovery Whitepaper.
6. Design a plan for how your workload will fail back.
Failback is when you return workload operation to the primary Region, after a disaster event has
abated. Provisioning infrastructure and code to the primary Region generally follows the same
steps as were initially used, relying on infrastructure as code and code deployment pipelines. The
challenge with failback is restoring data stores, and ensuring their consistency with the recovery
Region in operation.
In the failed over state, the databases in the recovery Region are live and have the up-to-
date data. The goal then is to re-synchronize from the recovery Region to the primary Region,
ensuring it is up-to-date.
Some AWS services will do this automatically. If using Amazon DynamoDB global tables,
even if the table in the primary Region had become not available, when it comes back online,
DynamoDB resumes propagating any pending writes. If using Amazon Aurora Global Database
and using managed planned failover, then Aurora global database's existing replication topology
