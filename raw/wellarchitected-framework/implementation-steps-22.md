---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 175
---

# Implementation steps

1. Document the policies that require teams to have effective plans to reverse changes within a
specified period.
a. Policies should specify when a fix-forward situation is allowed.
b. Require a documented rollback plan to be accessible by all involved.
c. Specify the requirements to rollback (for example, when it is found that unauthorized
changes have been deployed).
2. Analyze the level of impact of all changes related to each component of a workload.
a. Allow repeatable changes to be standardized, templated, and preauthorized if they follow a
consistent workflow that enforces change policies.
b. Reduce the potential impact of any change by making the size of the change smaller so
recovery takes less time and causes less business impact.
c. Ensure rollback procedures revert code to the known good state to avoid incidents where
possible.
3. Integrate tools and workflows to enforce your policies programatically.
4. Make data about changes visible to other workload owners to improve the speed of diagnosis of
any failed change that cannot be rolled back.
a. Measure success of this practice using visible change data and identify iterative
improvements.
5. Use monitoring tools to verify the success or failure of a deployment to speed up decision-
making on rolling back.
6. Measure your duration of outage during an unsuccessful change to continually improve your
recovery plans.
