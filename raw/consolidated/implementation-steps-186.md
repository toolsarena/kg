---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 839
---

# Implementation steps

• Define expected usage levels: To begin, focus on usage levels. Engage with the application
owners, marketing, and greater business teams to understand what the expected usage levels
are for the workload. How might customer demand change over time, and what can change due
to seasonal increases or marketing campaigns?
• Define workload resourcing and costs: With usage levels defined, quantify the changes in
workload resources required to meet those usage levels. You may need to increase the size or
number of resources for a workload component, increase data transfer, or change workload
components to a different service at a specific level. Specify the costs at each of these major
points, and predict the change in cost when there is a change in usage.
• Define business goals: Take the output from the expected changes in usage and cost, combine
this with expected changes in technology, or any programs that you are running, and develop
goals for the workload. Goals must address usage and cost, as well as the relationship between
the two. Goals must be simple, high-level, and help people understand what the business
expects in terms of outcomes (such as making sure unused resources are kept below certain cost
level). You don't need to define goals for each unused resource type or define costs that can
cause losses in goals and targets. Verify that there are organizational programs (for example,
capability building like training and education) if there are expected changes in cost without
changes in usage.
• Define targets: For each of the defined goals, specify a measurable target. If the goal is to
increase efficiency in the workload, the target should quantify the amount of improvement
(typically in business outputs for each dollar spent) and when it should be delivered. For
example, you could set a goal to minimize waste due to over-provisioning. With this goal,
your target can be that waste due to compute over-provisioning in the first tier of production
workloads should not exceed ten percent of tier compute cost. Additionally, a second target
could be that waste due to compute over-provisioning in the second tier of production
workloads should not exceed five percent of tier compute cost.


# Implementation steps

• Define separation requirements: Requirements for separation are a combination of multiple
factors, including security, reliability, and financial constructs. Work through each factor in order