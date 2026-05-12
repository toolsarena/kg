---
title: "Design principles"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 14
---

# Design principles

The following are design principles for operational excellence in the cloud:
• Organize teams around business outcomes: The ability of a team to achieve business outcomes
comes from leadership vision, effective operations, and a business-aligned operating model.
Leadership should be fully invested and committed to a CloudOps transformation with a suitable
cloud operating model that incentivizes teams to operate in the most efficient way and meet
business outcomes. The right operating model uses people, process, and technology capabilities
to scale, optimize for productivity, and differentiate through agility, responsiveness, and
adaptation. The organization's long-term vision is translated into goals that are communicated
across the enterprise to stakeholders and consumers of your cloud services. Goals and
operational KPIs are aligned at all levels. This practice sustains the long-term value derived from
implementing the following design principles.
• Implement observability for actionable insights: Gain a comprehensive understanding
of workload behavior, performance, reliability, cost, and health. Establish key performance
indicators (KPIs) and leverage observability telemetry to make informed decisions and take
prompt action when business outcomes are at risk. Proactively improve performance, reliability,
and cost based on actionable observability data.
• Safely automate where possible: In the cloud, you can apply the same engineering discipline
that you use for application code to your entire environment. You can define your entire
workload and its operations (applications, infrastructure, configuration, and procedures) as code,
and update it. You can then automate your workload’s operations by initiating them in response
to events. In the cloud, you can employ automation safety by configuring guardrails, including
rate control, error thresholds, and approvals. Through effective automation, you can achieve
consistent responses to events, limit human error, and reduce operator toil.
• Make frequent, small, reversible changes: Design workloads that are scalable and loosely
coupled to permit components to be updated regularly. Automated deployment techniques
together with smaller, incremental changes reduces the blast radius and allows for faster reversal
when failures occur. This increases confidence to deliver beneficial changes to your workload
while maintaining quality and adapting quickly to changes in market conditions.
• Refine operations procedures frequently: As you evolve your workloads, evolve your operations
appropriately. As you use operations procedures, look for opportunities to improve them. Hold
regular reviews and validate that all procedures are effective and that teams are familiar with
them. Where gaps are identified, update procedures accordingly. Communicate procedural
