---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 286
---

# AWS Well-Architected Framework Framework

This is where you identify threats to your system. Threats are accidental or intentional actions or
events that have unwanted impacts and could affect the security of your system. Without a clear
understanding of what could go wrong, you have no way of doing anything about it.
There is no canonical list of what can go wrong. Creating this list requires brainstorming and
collaboration between all of the individuals within your team and relevant personas involved in
the threat modeling exercise. You can aid your brainstorming by using a model for identifying
threats, such as STRIDE, which suggests different categories to evaluate: Spoofing, Tampering,
Repudiation, Information Disclosure, Denial of Service, and Elevation of privilege. In addition,
you might want to aid the brainstorming by reviewing existing lists and research for inspiration,
including the OWASP Top 10, HiTrust Threat Catalog, and your organization’s own threat
catalog.
3. What are we going to do about it?
As was the case with the previous question, there is no canonical list of all possible mitigations.
The inputs into this step are the identified threats, actors, and areas of improvement from the
previous step.
Security and compliance is a shared responsibility between you and AWS. It’s important
to understand that when you ask “What are we going to do about it?”, that you are also
asking “Who is responsible for doing something about it?”. Understanding the balance of
responsibilities between you and AWS helps you scope your threat modeling exercise to the
mitigations that are under your control, which are typically a combination of AWS service
configuration options and your own system-specific mitigations.
For the AWS portion of the shared responsibility, you will find that AWS services are in-scope of
many compliance programs. These programs help you to understand the robust controls in place
at AWS to maintain security and compliance of the cloud. The audit reports from these programs
are available for download for AWS customers from AWS Artifact.
Regardless of which AWS services you are using, there’s always an element of customer
responsibility, and mitigations aligned to these responsibilities should be included in your
threat model. For security control mitigations for the AWS services themselves, you want to
consider implementing security controls across domains, including domains such as identity and
access management (authentication and authorization), data protection (at rest and in transit),
infrastructure security, logging, and monitoring. The documentation for each AWS service has
a dedicated security chapter that provides guidance on the security controls to consider as
