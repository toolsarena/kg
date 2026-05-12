---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 145
---

# AWS Well-Architected Framework Framework

external databases, third-party APIs, network connectivity routes to other environments, and
DNS services. The first step towards effective dependency telemetry is being comprehensive in
understanding what those dependencies are.
2. Develop a monitoring strategy: Once you have a clear picture of your external dependencies,
architect a monitoring strategy tailored to them. This involves understanding the criticality of
each dependency, its expected behavior, and any associated service-level agreements or targets
(SLA or SLTs). Set up proactive alerts to notify you of status changes or performance deviations.
3. Use network monitoring: Use Internet Monitor and Network Monitor, which provide
comprehensive insights into global internet and network conditions. These tools help you
understand and respond to outages, disruptions, or performance degradations that affect your
external dependencies.
4. Stay informed with AWS Health: AWS Health is the authoritative source of information about
the health of your AWS Cloud resources. Use AWS Health to visualize and receive notifications
about any current service events and upcoming changes, such as planned lifecycle events, so you
can take steps to mitigate impacts.
a. Create purpose-fit AWS Health event notifications to e-mail and chat channels through AWS
User Notifications, and integrate programatically with your monitoring and alerting tools
through Amazon EventBridge or the AWS Health API.
b. Plan and track progress on health events that require action by integrating with change
management or ITSM tools (like Jira or ServiceNow) that you may already use through
Amazon EventBridge or the AWS Health API.
c. If you use AWS Organizations, enable organization view for AWS Health to aggregate AWS
Health events across accounts.
5. Instrument your application with AWS X-Ray: AWS X-Ray provides insights into how
applications and their underlying dependencies are performing. By tracing requests from start
to end, you can identify bottlenecks or failures in the external services or components your
application relies on.
6. Use Amazon DevOps Guru: This machine learning-driven service identifies operational issues,
predicts when critical issues might occur, and recommends specific actions to take. It's invaluable
for gaining insights into dependencies and ensuring they're not the source of operational
problems.
7. Monitor regularly: Continually monitor metrics and logs related to external dependencies. Set
up alerts for unexpected behavior or degraded performance.


# AWS Well-Architected Framework Framework

8. Validate after changes: Whenever there's an update or change in any of the external
dependencies, validate their performance and check their alignment with your application's
requirements.