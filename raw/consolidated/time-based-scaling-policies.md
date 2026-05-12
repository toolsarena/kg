---
title: "Time-based scaling policies"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 923
---

# Time-based scaling policies

You can use scheduled or predictive auto scaling to implement a time-based approach. Workloads
can be scheduled to scale out or in at defined times (for example, the start of business hours),
making resources available when users arrive or demand increases. Predictive scaling uses patterns
to scale out while scheduled scaling uses pre-defined times to scale out. You can also use attribute-
based instance type selection (ABS) strategy in Auto Scaling groups, which lets you express your
instance requirements as a set of attributes, such as vCPU, memory, and storage. This also allows
you to automatically use newer generation instance types when they are released and access a
broader range of capacity with Amazon EC2 Spot Instances. Amazon EC2 Fleet and Amazon EC2
Auto Scaling select and launch instances that fit the specified attributes, removing the need to
manually pick instance types.
You can also leverage the AWS APIs and SDKs and AWS CloudFormation to automatically provision
and decommission entire environments as you need them. This approach is well suited for
development or test environments that run only in defined business hours or periods of time. You
can use APIs to scale the size of resources within an environment (vertical scaling). For example,
you could scale up a production workload by changing the instance size or class. This can be
achieved by stopping and starting the instance and selecting the different instance size or class.
This technique can also be applied to other resources, such as Amazon EBS Elastic Volumes, which
can be modified to increase size, adjust performance (IOPS) or change the volume type while in
use.


# Time Series database Amazon Timestream Used to efficiently collect,

synthesize, and derive
insights from data that
changes over time. IoT
applications, DevOps, and
industrial telemetry can
utilize time-series databases.

# Time Series database Amazon Timestream Used to efficiently collect,

synthesize, and derive
insights from data that
changes over time. IoT
applications, DevOps, and
industrial telemetry can
utilize time-series databases.