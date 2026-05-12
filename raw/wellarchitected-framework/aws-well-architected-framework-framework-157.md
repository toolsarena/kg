---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 213
---

# AWS Well-Architected Framework Framework

3. Implement actionable alerts: Design alerts that provide adequate information for immediate
action.
1. Monitor AWS Health events with Amazon EventBridge rules, or integrate programatically with
the AWS Health API to automate actions when you receive AWS Health events. These can be
general actions, such as sending all planned lifecycle event messages to a chat interface, or
specific actions, such as the initiation of a workflow in an IT service management tool.
4. Reduce alert fatigue: Minimize non-critical alerts. When teams are overwhelmed with numerous
insignificant alerts, they can lose oversight of critical issues, which diminishes the overall
effectiveness of the alert mechanism.
5. Set up composite alarms: Use Amazon CloudWatch composite alarms to consolidate multiple
alarms.
6. Integrate with alert tools: Incorporate tools like Ops Genie and PagerDuty.
7. Engage Amazon Q Developer in chat applications: Integrate Amazon Q Developer in chat
applications to relay alerts to Amazon Chime, Microsoft Teams, and Slack.
8. Alert based on logs: Use log metric filters in CloudWatch to create alarms based on specific log
events.
9. Review and iterate: Regularly revisit and refine alert configurations.
