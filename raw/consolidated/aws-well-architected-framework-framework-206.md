---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 280
---

# AWS Well-Architected Framework Framework

for orchestrating containers, or using serverless options. When building new applications, think
through which services can help reduce time and cost when it comes to implementing and
managing security controls.
Compliance requirements can also be a factor when selecting services. Managed services can shift
the compliance of some requirements to AWS. Discuss with your compliance team about their
degree of comfort with auditing the aspects of services you operate and manage and accepting
control statements in relevant AWS audit reports. You can provide the audit artifacts found in AWS
Artifact to your auditors or regulators as evidence of AWS security controls. You can also use the
responsibility guidance provided by some of the AWS audit artifacts to design your architecture,
along with the AWS Customer Compliance Guides. This guidance helps determine the additional
security controls you should put in place in order to support the specific use cases of your system.
When using managed services, be familiar with the process of updating their resources to
newer versions (for example, updating the version of a database managed by Amazon RDS, or a
programming language runtime for an AWS Lambda function). While the managed service may
perform this operation for you, configuring the timing of the update and understanding the impact
on your operations remains your responsibility. Tools like AWS Health can help you track and
manage these updates throughout your environments.


# AWS Well-Architected Framework Framework

• PERF02-BP01 Select the best compute options for your workload
• PERF03-BP01 Use a purpose-built data store that best supports your data access and storage
requirements
• SUS05-BP03 Use managed services