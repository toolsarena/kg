---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 802
---

# Implementation steps

• Identify remediation workflow: Identify and understand the performance issue that can be
remediated automatically. Use AWS monitoring solutions such as Amazon CloudWatch or AWS X-
Ray to help you better understand the root cause of the issue.
• Define the automation process: Create a step-by-step remediation process that can be used to
automatically fix the issue.
• Configure the initiation event: Configure the event to automatically initiate the remediation
process. For example, you can define a trigger to automatically restart an instance when it
reaches a certain threshold of CPU utilization.
• Automate the remediation: Use AWS services and technologies to automate the remediation
process. For example, AWS Systems Manager Automation provides a secure and scalable way to
automate the remediation process. Make sure to use self-healing logic to revert changes if they
do not successfully resolve the issue.
• Test the workflow Test the automated remediation process in a pre-production environment.
• Implement the workflow: Implement the automated remediation in the production
environment.
• Develop a playbook: Develop and document a playbook that outlines the steps for the
remediation plan, including the initiation events, remediation logic, and actions taken. Make sure
to train stakeholders to help them effectively respond to automated remediation events.
