---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 23
---

# AWS Well-Architected Framework Framework

Efficient and effective management of operational events is required to achieve operational
excellence. This applies to both planned and unplanned operational events. Use established
runbooks for well-understood events, and use playbooks to aid in investigation and resolution of
issues. Prioritize responses to events based on their business and customer impact. Verify that if
an alert is raised in response to an event, there is an associated process to run with a specifically
identified owner. Define in advance the personnel required to resolve an event and include
escalation processes to engage additional personnel, as it becomes necessary, based on urgency
and impact. Identify and engage individuals with the authority to make a decision on courses of
action where there will be a business impact from an event response not previously addressed.
Communicate the operational status of workloads through dashboards and notifications that are
tailored to the target audience (for example, customer, business, developers, operations) so that
they may take appropriate action, so that their expectations are managed, and so that they are
informed when normal operations resume.
In AWS, you can generate dashboard views of your metrics collected from workloads and natively
from AWS. You can leverage CloudWatch or third-party applications to aggregate and present
business, workload, and operations level views of operations activities. AWS provides workload
insights through logging capabilities including AWS X-Ray, CloudWatch, CloudTrail, and VPC Flow
Logs to identify workload issues in support of root cause analysis and remediation.
The following questions focus on these considerations for operational excellence.
OPS 8: How do you utilize workload observability in your organization?
Ensure optimal workload health by leveraging observability. Utilize relevant metrics, logs, and
traces to gain a comprehensive view of your workload's performance and address issues efficient
ly.
OPS 9: How do you understand the health of your operations?
Define, capture, and analyze operations metrics to gain visibility to operations events so that
you can take appropriate action.
