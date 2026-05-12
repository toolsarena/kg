---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 480
---

# Implementation guidance

Unlike soft service quotas or resources that be replaced with higher capacity units, AWS services’
fixed quotas cannot be changed. This means that all these type of AWS services must be evaluated
for potential hard capacity limits when used in an application design.
Hard limits are shown in the Service Quotas console. If the columns shows ADJUSTABLE = No,
the service has a hard limit. Hard limits are also shown in some resources configuration pages. For
example, Lambda has specific hard limits that cannot be adjusted.
As an example, when designing a python application to run in a Lambda function, the application
should be evaluated to determine if there is any chance of Lambda running longer than 15
minutes. If the code may run more than this service quota limit, alternate technologies or designs
must be considered. If this limit is reached after production deployment, the application will suffer
degradation and disruption until it can be remediated. Unlike soft quotas, there is no method to
change to these limits even under emergency Severity 1 events.
Once the application has been deployed to a testing environment, strategies should be used to find
if any hard limits can be reached. Stress testing, load testing, and chaos testing should be part of
the introduction test plan.
