---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 426
---

# Implementation guidance

An incident management plan is critical to respond, mitigate, and recover from the potential
impact of security incidents. An incident management plan is a structured process for identifying,
remediating, and responding in a timely matter to security incidents.
The cloud has many of the same operational roles and requirements found in an on-premises
environment. When you create an incident management plan, it is important to factor response
and recovery strategies that best align with your business outcome and compliance requirements.
For example, if you operate workloads in AWS that are FedRAMP compliant in the United States,
follow the recommendations in NIST SP 800-61 Computer Security Handling Guide. Similarly, when
you operate workloads that store personally identifiable information (PII), consider how to protect
and respond to issues related to data residency and use.
When building an incident management plan for your workloads in AWS, start with the AWS
Shared Responsibility Model for building a defense-in-depth approach towards incident response.
In this model, AWS manages security of the cloud, and you are responsible for security in the cloud.
This means that you retain control and are responsible for the security controls you choose to
implement. The AWS Security Incident Response Guide details key concepts and foundational
guidance for building a cloud-centric incident management plan.
An effective incident management plan must be continually iterated upon, remaining current with
your cloud operations goal. Consider using the implementation plans detailed below as you create
and evolve your incident management plan.
