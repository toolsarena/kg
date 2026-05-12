---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 439
---

# Implementation guidance

To automate security response and operations functions, you can use a comprehensive set of
APIs and tools from AWS. You can fully automate identity management, network security, data
protection, and monitoring capabilities and deliver them using popular software development
methods that you already have in place. When you build security automation, your system can
monitor, review, and initiate a response, rather than having people monitor your security position
and manually react to events.
If your incident response teams continue to respond to alerts in the same way, they risk alert
fatigue. Over time, the team can become desensitized to alerts and can either make mistakes
handling ordinary situations or miss unusual alerts. Automation helps avoid alert fatigue by
using functions that process the repetitive and ordinary alerts, leaving humans to handle the
sensitive and unique incidents. Integrating anomaly detection systems, such as Amazon GuardDuty,
AWS CloudTrail Insights, and Amazon CloudWatch Anomaly Detection, can reduce the burden of
common threshold-based alerts.
You can improve manual processes by programmatically automating steps in the process. After
you define the remediation pattern to an event, you can decompose that pattern into actionable
logic, and write the code to perform that logic. Responders can then run that code to remediate
the issue. Over time, you can automate more and more steps, and ultimately automatically handle
whole classes of common incidents.
During a security investigation, you need to be able to review relevant logs to record and
understand the full scope and timeline of the incident. Logs are also required for alert generation,
indicating certain actions of interest have happened. It is critical to select, enable, store, and set up
querying and retrieval mechanisms, and set up alerting. Additionally, an effective way to provide
tools to search log data is Amazon Detective.
AWS offers over 200 cloud services and thousands of features. We recommend that you review the
services that can support and simplify your incident response strategy.
In addition to logging, you should develop and implement a tagging strategy. Tagging can help
provide context around the purpose of an AWS resource. Tagging can also be used for automation.
