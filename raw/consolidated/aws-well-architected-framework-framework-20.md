---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 32
---

# AWS Well-Architected Framework Framework

important reactive factors that can help your organization identify and understand the scope of
anomalous activity.
In AWS, you can implement detective controls by processing logs, events, and monitoring that
allows for auditing, automated analysis, and alarming. CloudTrail logs, AWS API calls, and
CloudWatch provide monitoring of metrics with alarming, and AWS Config provides configuration
history. Amazon GuardDuty is a managed threat detection service that continuously monitors for
malicious or unauthorized behavior to help you protect your AWS accounts and workloads. Service-
level logs are also available, for example, you can use Amazon Simple Storage Service (Amazon S3)
to log access requests.
The following question focuses on these considerations for security.
SEC 4: How do you detect and investigate security events?
Capture and analyze events from logs and metrics to gain visibility. Take action on security
events and potential threats to help secure your workload.
Log management is important to a Well-Architected workload for reasons ranging from security
or forensics to regulatory or legal requirements. It is critical that you analyze logs and respond to
them so that you can identify potential security incidents. AWS provides functionality that makes
log management easier to implement by giving you the ability to define a data-retention lifecycle
or define where data will be preserved, archived, or eventually deleted. This makes predictable and
reliable data handling simpler and more cost effective.
