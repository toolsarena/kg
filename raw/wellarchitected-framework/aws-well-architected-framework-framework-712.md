---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 932
---

# AWS Well-Architected Framework Framework

with the capabilities of AWS Config and AWS CloudFormation, you can efficiently manage and
automate configuration compliance at scale for hundreds of member accounts. You can review
changes in configurations and relationships between AWS resources and dive into the history of
a resource configuration.
• Automate monitoring tasks AWS provides various tools that you can use to monitor services.
You can configure these tools to automate monitoring tasks. Create and implement a monitoring
plan that collects monitoring data from all the parts in your workload so that you can more
easily debug a multi-point failure if one occurs. For example, you can use the automated
monitoring tools to observe Amazon EC2 and report back to you when something is wrong for
system status checks, instance status checks, and Amazon CloudWatch alarms.
• Automate maintenance and operations: Run routine operations automatically without
human intervention. Using AWS services and tools, you can choose which AWS automations to
implement and customize for your specific requirements. For example, use EC2 Image Builder for
building, testing, and deployment of virtual machine and container images for use on AWS or
on-premises or patching your EC2 instances with AWS SSM. If your desired action cannot be done
with AWS services or you need more complex actions with filtering resources, then automate
your operations by using AWS Command Line Interface (AWS CLI) or AWS SDK tools. AWS CLI
provides the ability to automate the entire process of controlling and managing AWS services
with scripts without using the AWS Management Console. Select your preferred AWS SDKs to
interact with AWS services. For other code examples, see AWS SDK Code examples repository.
• Create a continual lifecycle with automations: It is important that you establish and preserve
mature lifecycle policies not only for regulations or redundancy but also for cost optimization.
You can use AWS Backup to centrally manage and automate data protection of data stores, such
as your buckets, volumes, databases, and file systems. You can also use Amazon Data Lifecycle
Manager to automate the creation, retention, and deletion of EBS snapshots and EBS-backed
AMIs.
• Delete unnecessary resources: It's quite common to accumulate unused resources in sandbox
or development AWS accounts. Developers create and experiment with various services and
resources as part of the normal development cycle, and then they don't delete those resources
when they're no longer needed. Unused resources can incur unnecessary and sometimes high
costs for the organization. Deleting these resources can reduce the costs of operating these
environments. Make sure your data is not needed or backed up if you are not sure. You can use
AWS CloudFormation to clean up deployed stacks, which automatically deletes most resources
defined in the template. Alternatively, you can create an automation for the deletion of AWS
resources using tools like aws-nuke.
