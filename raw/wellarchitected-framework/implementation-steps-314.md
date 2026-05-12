---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 349
---

# Implementation steps

• Select and use log sources. Ahead of a security investigation, you need to capture relevant
logs to retroactively reconstruct activity in an AWS account. Select log sources relevant to your
workloads.
The log source selection criteria should be based on the use cases required by your business.
Establish a trail for each AWS account using AWS CloudTrail or an AWS Organizations trail, and
configure an Amazon S3 bucket for it.
AWS CloudTrail is a logging service that tracks API calls made against an AWS account capturing
AWS service activity. It’s turned on by default with a 90-day retention of management events
that can be retrieved through CloudTrail Event history using the AWS Management Console, the
AWS CLI, or an AWS SDK. For longer retention and visibility of data events, create a CloudTrail
trail and associate it with an Amazon S3 bucket, and optionally with a Amazon CloudWatch log
group. Alternatively, you can create a CloudTrail Lake, which retains CloudTrail logs for up to
seven years and provides a SQL-based querying facility
AWS recommends that customers using a VPC turn on network traffic and DNS logs using VPC
Flow Logs and Amazon Route 53 resolver query logs, respectively, and streaming them to either
an Amazon S3 bucket or a CloudWatch log group. You can create a VPC flow log for a VPC, a
subnet, or a network interface. For VPC Flow Logs, you can be selective on how and where you
use Flow Logs to reduce cost.
AWS CloudTrail Logs, VPC Flow Logs, and Route 53 resolver query logs are the basic logging
sources to support security investigations in AWS. You can also use Amazon Security Lake to
collect, normalize, and store this log data in Apache Parquet format and Open Cybersecurity
