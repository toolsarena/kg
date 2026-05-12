---
title: "Maintain consistency and atomicity by using appropriate concurrency control mechanisms"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 534
---

# Maintain consistency and atomicity by using appropriate concurrency control mechanisms

if needed, such as locks, transactions, or optimistic concurrency controls. This includes the
process of recording the idempotent token and running all mutating operations associated with
servicing the request. This helps prevent race conditions and verifies that idempotent operations
run correctly.
Regularly remove old idempotency tokens from the datastore to manage storage and
performance. If your storage system supports it, consider using expiration timestamps for
data (often known as time to live, or TTL values). The likelihood of idempotency token reuse
diminishes over time.
Common AWS storage options typically used for storing idempotency tokens and related state
include:
• Amazon DynamoDB: DynamoDB is a NoSQL database service that provides low-latency
performance and high availability, which makes it well-suited for the storage of idempotency-
related data. The key-value and document data model of DynamoDB allows for efficient
storage and retrieval of idempotency tokens and associated state information. DynamoDB
can also expire idempotency tokens automatically if your application sets a TTL value when it
inserts them.
• Amazon ElastiCache: ElastiCache can store idempotency tokens with high throughput, low
latency, and at low cost. Both ElastiCache (Redis) and ElastiCache (Memcached) can also expire
idempotency tokens automatically if your application sets a TTL value when it inserts them.
• Amazon Relational Database Service (RDS): You can use Amazon RDS to store idempotency
tokens and related state information, especially if your application already uses a relational
database for other purposes.
• Amazon Simple Storage Service (S3): Amazon S3 is a highly scalable and durable object
storage service that can be used to store idempotency tokens and related metadata. The
versioning capabilities of S3 can be particularly useful for maintenance of the state of
idempotent operations. The choice of storage service typically depends on factors such as the
volume of idempotency-related data, the required performance characteristics, the need for
durability and availability, and how the idempotency mechanism integrates with the overall
workload architecture.


# Major update Added Sustainability Pillar December 2, 2021

and updated links.

# Major update Added Sustainability Pillar December 2, 2021

and updated links.

# Major update Best practices updated with April 10, 2023

prescriptive guidance and
new best practices added.

# Major update Best practices updated with April 10, 2023

prescriptive guidance and
new best practices added.

# Major update Best practices were updated November 6, 2024

with new guidance in Reliabili
ty, Security, Operational
excellence, Sustainability,
and Performance efficiency.

# Major update Best practices were updated November 6, 2024

with new guidance in Reliabili
ty, Security, Operational
excellence, Sustainability,
and Performance efficiency.

# Major update Large-scale best practice June 27, 2024

updates were made
throughout the pillars.

# Major update Large-scale best practice June 27, 2024

updates were made
throughout the pillars.

# Major update Review and rewrite of most July 8, 2020

questions and answers.

# Major update Review and rewrite of most July 8, 2020

questions and answers.

# Major update Sustainability Pillar added to November 20, 2021

the framework.

# Major update Sustainability Pillar added to November 20, 2021

the framework.

# Make sure to choose the right network metric

for your workload. For example, you can turn
on metrics for VPC Network Address Usage,

# Make sure to choose the right network metric

for your workload. For example, you can turn
on metrics for VPC Network Address Usage,