---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 375
---

# Implementation guidance

Vulnerability management is a key aspect of maintaining a secure and robust cloud environment.
It involves a comprehensive process that includes security scans, identification and prioritization
of issues, and patch operations to resolve the identified vulnerabilities. Automation plays a pivotal
role in this process because it facilitates continuous scanning of workloads for potential issues and
unintended network exposure, as well as remediation efforts.
The AWS Shared Responsibility Model is a fundamental concept that underpins vulnerability
management. According to this model, AWS is responsible for securing the underlying
infrastructure, including hardware, software, networking, and facilities that run AWS services.
Conversely, you are responsible for securing your data, security configurations, and management
tasks associated with services like Amazon EC2 instances and Amazon S3 objects.
AWS offers a range of services to support vulnerability management programs. Amazon Inspector
continuously scans AWS workloads for software vulnerabilities and unintended network access,
while AWS Systems Manager Patch Manager helps manage patching across Amazon EC2
instances. These services can be integrated with AWS Security Hub CSPM, a cloud security posture
management service that automates AWS security checks, centralizes security alerts, and provides
a comprehensive view of an organization's security posture. Furthermore, Amazon CodeGuru
Security uses static code analysis to identify potential issues in Java and Python applications during
the development phase.
By incorporating vulnerability management practices into the software development lifecycle, you
can proactively address vulnerabilities before they are introduced into production environments,
which reduces the risk of security events and minimizes the potential impact of vulnerabilities.
