---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 435
---

# Implementation guidance

AWS recommends reducing or eliminating reliance on long-lived credentials wherever possible,
in favor of temporary credentials and just-in-time privilege escalation mechanisms. Long-lived
credentials are prone to security risk and increase operational overhead. For most management
tasks, as well as incident response tasks, we recommend you implement identity federation
alongside temporary escalation for administrative access. In this model, a user requests elevation
to a higher level of privilege (such as an incident response role) and, provided the user is eligible
for elevation, a request is sent to an approver. If the request is approved, the user receives a set
of temporary AWS credentials which can be used to complete their tasks. After these credentials
expire, the user must submit a new elevation request.
We recommend the use of temporary privilege escalation in the majority of incident response
scenarios. The correct way to do this is to use the AWS Security Token Service and session policies
to scope access.
