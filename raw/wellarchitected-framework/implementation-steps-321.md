---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 376
---

# Implementation steps

1. Understand the shared responsibility model: Review the AWS shared responsibility model
to understand your responsibilities for securing your workloads and data in the cloud. AWS
is responsible for securing the underlying cloud infrastructure, while you are responsible for
securing your applications, data, and the services you use.
2. Implement vulnerability scanning: Configure a vulnerability scanning service, such as Amazon
Inspector, to automatically scan your compute instances (for example, virtual machines,
containers, or serverless functions) for software vulnerabilities, potential defects, and
unintended network exposure.
3. Establish vulnerability management processes: Define processes and procedures to identify,
prioritize, and remediate vulnerabilities. This may include the setup of regular vulnerability
scanning schedules, establishment of risk assessment criteria, and definition of remediation
timelines based on vulnerability severity.
4. Set up patch management: Use a patch management service to automate the process of
patching your compute instances, both for operating systems and applications. You can
configure the service to scan instances for missing patches and automatically install them on a
schedule. Consider AWS Systems Manager Patch Manager to provide this functionality.
5. Configure malware protection: Implement mechanisms to detect malicious software in your
environment. For example, you can use tools like Amazon GuardDuty to analyze, detect, and
alert of malware in EC2 and EBS volumes. GuardDuty can also scan newly uploaded objects to
Amazon S3 for potential malware or viruses and take action to isolate them before they are
ingested into downstream processes.
6. Integrate vulnerability scanning in CI/CD pipelines: If you're using a CI/CD pipeline for your
application deployment, integrate vulnerability scanning tools into your pipeline. Tools like
Amazon CodeGuru Security and open-source options can scan your source code, dependencies,
and artifacts for potential security issues.
7. Configure a security monitoring service: Set up a security monitoring service, such as AWS
Security Hub CSPM, to get a comprehensive view of your security posture across multiple cloud
services. The service should collect security findings from various sources and present them in a
standardized format for easier prioritization and remediation.
8. Implement web application penetration testing: If your application is a web application, and
your organization has the necessary skills or can hire outside assistance, consider implementing
web application penetration testing to identify potential vulnerabilities in your application.
