---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 867
---

# AWS Well-Architected Framework Framework

• Create and implement a decommissioning process: Work with the workload developers and
owners to build a decommissioning process for the workload and its resources. The process
should cover the method to verify if the workload is in use, and also if each of the workload
resources are in use. Detail the steps necessary to decommission the resource, removing them
from service while ensuring compliance with any regulatory requirements. Any associated
resources should be included, such as licenses or attached storage. Notify the workload owners
that the decommissioning process has been started.
Use the following decommission steps to guide you on what should be checked as part of your
process:
• Identify resources to be decommissioned: Identify resources that are eligible for
decommissioning in your AWS Cloud. Record all necessary information and schedule the
decommission. In your timeline, be sure to account for if (and when) unexpected issues arise
during the process.
• Coordinate and communicate: Work with workload owners to confirm the resource to be
decommissioned
• Record metadata and create backups: Record metadata (such as public IPs, Region, AZ,
VPC, Subnet, and Security Groups) and create backups (such as Amazon Elastic Block Store
snapshots or taking AMI, keys export, and Certificate export) if it is required for the resources
in the production environment or if they are critical resources.
• Validate infrastructure-as-code: Determine whether resources were deployed with
CloudFormation, Terraform, AWS Cloud Development Kit (AWS CDK), or any other
infrastructure-as-code deployment tool so they can be re-deployed if necessary.
• Prevent access: Apply restrictive controls for a period of time, to prevent the use of resources
while you determine if the resource is required. Verify that the resource environment can be
reverted to its original state if required.
• Follow your internal decommissioning process: Follow the administrative tasks and
decommissioning process of your organization, like removing the resource from your
organization domain, removing the DNS record, and removing the resource from your
configuration management tool, monitoring tool, automation tool and security tools.
If the resource is an Amazon EC2 instance, consult the following list. For more detail, see How do
I delete or terminate my Amazon EC2 resources?
• Stop or terminate all your Amazon EC2 instances and load balancers. Amazon EC2 instances
are visible in the console for a short time after they're terminated. You aren't billed for any
instances that aren't in the running state
