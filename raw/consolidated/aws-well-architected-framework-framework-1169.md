---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 548
---

# AWS Well-Architected Framework Framework

• Not clearing backlogged messages from a queue, when there is no value in processing these
messages if the business need no longer exists.
• Configuring first in first out (FIFO) queues when last in first out (LIFO) queues would better serve
client needs, for example when strict ordering is not required and backlog processing is delaying
all new and time sensitive requests resulting in all clients experiencing breached service levels.
• Exposing internal queues to clients instead of exposing APIs that manage work intake and place
requests into internal queues.
• Combining too many work request types into a single queue which can exacerbate backlog
conditions by spreading resource demand across request types.
• Processing complex and simple requests in the same queue, despite needing different
monitoring, timeouts and resource allocations.
• Not validating inputs or using assertions to implement fail fast mechanisms in software that
bubble up exceptions to higher level components that can handle errors gracefully.
• Not removing faulty resources from request routing, especially when failures are grey emitting
both successes and failures due to crashing and restarting, intermittent dependency failure,
reduced capacity, or network packet loss.
Benefits of establishing this best practice: Systems that fail fast are easier to debug and fix, and
often expose issues in coding and configuration before releases are published into production.
Systems that incorporate effective queueing strategies provide greater resilience and reliability to
traffic spikes and intermittent system fault conditions.
Level of risk exposed if this best practice is not established: High


# AWS Well-Architected Framework Framework

For dynamic configurations in your applications running on Amazon EC2 instances, AWS Lambda,
containers, mobile applications, or IoT devices, you can use AWS AppConfig to configure, validate,
deploy, and monitor them across your environments.

# AWS Well-Architected Framework Framework

• Avoiding insurmountable queue backlogs
• Fail Fast
• How can I prevent an increasing backlog of messages in my Amazon SQS queue?
• Elastic Load Balancing: Zonal Shift
• Amazon Application Recovery Controller: Routing control for traffic failover