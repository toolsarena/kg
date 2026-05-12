---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 392
---

# Implementation guidance

Implementing data protection controls based on data sensitivity levels involves several key steps.
First, identify the different data sensitivity levels within your workload architecture (such as public,
internal, confidential, and restricted) and evaluate where you store and process this data. Next,
define isolation boundaries around data based on its sensitivity level. We recommend you separate
data into different AWS accounts, using service control policies (SCPs) to restrict services and
actions allowed for each data sensitivity level. This way, you can create strong isolation boundaries
and enforce the principle of least privilege.
After you define the isolation boundaries, implement appropriate protection controls based on
the data sensitivity levels. Refer to best practices for Protecting data at rest and Protecting data
in transit to implement relevant controls like encryption, access controls, and auditing. Consider
techniques like tokenization or anonymization to reduce the sensitivity level of your data. Simplify
applying consistent data policies across your business with a centralized system for tokenization
and de-tokenization.
Continuously monitor and test the effectiveness of the implemented controls. Regularly review
and update the data classification scheme, risk assessments, and protection controls as your
organization's data landscape and threats evolve. Align the implemented data protection controls
with relevant industry regulations, standards, and legal requirements. Further, provide security
awareness and training to help employees understand the data classification scheme and their
responsibilities in handling and protecting sensitive data.
