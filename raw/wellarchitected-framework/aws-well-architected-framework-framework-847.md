---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 125
---

# AWS Well-Architected Framework Framework

13.Prioritize actions that are repeatable where possible to safely automate at scale.
14.When communications are required in scenarios with automated actions, the communication's
purpose should be to inform teams, for auditing, or a part of the change management process.
15.Analyze communications from your alert systems for false positives or alerts that are constantly
created. Remove or change these alerts so that they start when human intervention is required.
If an alert is initiated, provide a runbook or playbook.
a. You can use AWS Systems Manager Documents to build playbooks and runbooks for alerts.
16.Mechanisms are in place to provide notification of risks or planned events in a clear and
actionable way with enough notice to allow appropriate responses. Use email lists or chat
channels to send notifications ahead of planned events.
a. AWS Chatbot can be used to send alerts and respond to events within your organizations
messaging platform.
17.Provide an accessible source of information where planned events can be discovered. Provide
notifications of planned events from the same system.
a. AWS Systems Manager Change Calendar can be used to create change windows when
changes can occur. This provides team members notice when they can make changes safely.
18.Monitor vulnerability notifications and patch information to understand vulnerabilities in the
wild and potential risks associated to your workload components. Provide notification to team
members so that they can act.
a. You can subscribe to AWS Security Bulletins to receive notifications of vulnerabilities on AWS.
19.Seek diverse opinions and perspectives: Encourage contributions from everyone. Give
communication opportunities to under-represented groups. Rotate roles and responsibilities in
meetings.
a. Expand roles and responsibilities: Provide opportunities for team members to take on roles
that they might not otherwise. They can gain experience and perspective from the role and
from interactions with new team members with whom they might not otherwise interact.
They can also bring their experience and perspective to the new role and team members
they interact with. As perspective increases, identify emergent business opportunities or new
opportunities for improvement. Rotate common tasks between members within a team that
others typically perform to understand the demands and impact of performing them.
b. Provide a safe and welcoming environment: Establish policy and controls that protect the
mental and physical safety of team members within your organization. Team members should
be able to interact without fear of reprisal. When team members feel safe and welcome, they
are more likely to be engaged and productive. The more diverse your organization, the better
