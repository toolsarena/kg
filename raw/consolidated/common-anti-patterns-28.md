---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 171
---

# Common anti-patterns:

• You deploy a new version of your application quarterly with a change window that means a core
service is turned off.
• You frequently make changes to your database schema without tracking changes in your
management systems.
• You perform manual in-place updates, overwriting existing installations and configurations, and
have no clear roll-back plan.
Benefits of establishing this best practice: Development efforts are faster by deploying small
changes frequently. When the changes are small, it is much easier to identify if they have
unintended consequences, and they are easier to reverse. When the changes are reversible, there is
less risk to implementing the change, as recovery is simplified. The change process has a reduced
risk and the impact of a failed change is reduced.
Level of risk exposed if this best practice is not established: Low


# Common anti-patterns:

• Engineers joining an incident management call require status updates to get up to speed.
• Relying on manual reporting for management, which leads to delays and potential inaccuracies.
• Operations teams are frequently interrupted for status updates during incidents.

# Common anti-patterns:

• Manual event handling leads to delays and errors.
• Automation is overlooked in repetitive, critical tasks.
• Repetitive, manual tasks lead to alert fatigue and missing critical issues.