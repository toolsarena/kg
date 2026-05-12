---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 183
---

# Implementation guidance

Automate testing of deployed environments to confirm desired outcomes more quickly. Automate
rollback to a previous known good state when pre-defined outcomes are not achieved to minimize
recovery time and reduce errors caused by manual processes. Integrate testing tools with your
pipeline workflow to consistently test and minimize manual inputs. Prioritize automating test
cases, such as those that mitigate the greatest risks and need to be tested frequently with every
change. Additionally, automate rollback based on specific conditions that are pre-defined in your
test plan.


# Implementation guidance

Properly defined escalation paths are crucial for rapid incident response. AWS Systems Manager
Incident Manager supports the setup of structured escalation plans and on-call schedules, which
alert the right personnel so that they are ready to act when incidents occur.

# Implementation guidance

Creating a comprehensive communication plan for service impacting events involves multiple
facets, from choosing the right channels to crafting the message and tone. The plan should be
adaptable, scalable, and cater to different outage scenarios.