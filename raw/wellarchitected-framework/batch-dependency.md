---
title: "Batch dependency"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 524
---

# Batch dependency

Batch systems take input data, initiate a series of jobs to process it, and produce some output data,
without manual intervention. Depending on the data size, jobs could run from minutes to, in some
cases, several days. When your workload communicates with its batch dependency, consider the
following guidance:
• Define the time window when your workload should run the batch job. Your workload can set
up a recurrence pattern to invoke a batch system, for example, every hour or at the end of every
month.
• Determine the location of the data input and the processed data output. Choose a storage
service, such as Amazon Simple Storage Services (Amazon S3), Amazon Elastic File System
(Amazon EFS), and Amazon FSx for Lustre, that allows your workload to read and write files at
scale.
• If your workload needs to invoke multiple batch jobs, you could leverage AWS Step Functions
to simplify the orchestration of batch jobs that run in AWS or on-premises. This sample project
demonstrates orchestration of batch jobs using Step Functions, AWS Batch, and Lambda.
• Monitor batch jobs to look for abnormalities, such as a job taking longer than it should to
complete. You could use tools like CloudWatch Container Insights to monitor AWS Batch
environments and jobs. In this instance, your workload would stop the next job from beginning
and inform the relevant staff of the exception.
