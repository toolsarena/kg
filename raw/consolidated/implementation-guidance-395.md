---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 381
---

# Implementation guidance

Logging into an instance is a classic approach to system administration. After installing the server
operating system, users would typically log in manually to configure the system and install the
desired software. During the server's lifetime, users might log in to perform software updates,
apply patches, change configurations, and troubleshoot problems.
Manual access poses a number of risks, however. It requires a server that listens for requests, such
as an SSH or RDP service, that can provide a potential path to unauthorized access. It also increases
the risk of human error associated with performing manual steps. These can result in workload
incidents, data corruption or destruction, or other security issues. Human access also requires
protections against the sharing of credentials, creating additional management overhead.
To mitigate these risks, you can implement an agent-based remote access solution, such as AWS
Systems Manager. AWS Systems Manager Agent (SSM Agent) initiates an encrypted channel and
thus does not rely on listening for externally-initiated requests. Consider configuring SSM Agent to
establish this channel over a VPC endpoint.
Systems Manager gives you fine-grained control over how you can interact with your managed
instances. You define the automations to run, who can run them, and when they can run. Systems
Manager can apply patches, install software, and make configuration changes without interactive
access to the instance. Systems Manager can also provide access to a remote shell and log every
command invoked, and its output, during the session to logs and Amazon S3. AWS CloudTrail
records invocations of Systems Manager APIs for inspection.
