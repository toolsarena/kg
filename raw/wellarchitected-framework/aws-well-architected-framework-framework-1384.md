---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 836
---

# AWS Well-Architected Framework Framework

indicators (KPIs) can include things like percent of spend on-demand or adoption of certain
optimized services such as AWS Graviton instances or gp3 EBS volume types. Set measurable
and achievable goals to help you measure efficiency improvements, which is important for your
business operations. Goals provide guidance and direction to your organization on expected
outcomes.
Targets provide specific, measurable outcomes to be achieved. In short, a goal is the direction you
want to go, and a target is how far in that direction and when that goal should be achieved (use
guidance of specific, measurable, assignable, realistic and timely, or SMART). An example of a goal
is that platform usage should increase significantly, with only a minor (non-linear) increase in cost.
An example target is a 20% increase in platform usage, with less than a five percent increase in
costs. Another common goal is that workloads need to be more efficient every six months. The
accompanying target would be that the cost per business metrics needs to decrease by five percent
every six months. Use the right metrics, and set calculated KPIs for your organization. You can start
with basic KPIs and evolve later based on business needs.
A goal for cost optimization is to increase workload efficiency, which corresponds to a decrease in
the cost per business outcome of the workload over time. Implement this goal for all workloads,
and set a target like a five percent increase in efficiency every six months to a year. In the cloud,
you can achieve this through the establishment of capability in cost optimization, as well as new
service and feature releases.
Targets are the quantifiable benchmarks you want to reach to meet your goals and benchmarks
compare your actual results against a target. Establish benchmarks with KPIs for the cost per
unit of compute services (such as Spot adoption, Graviton adoption, latest instance types, and
On-Demands coverage), storage services (such as EBS GP3 adoption, obsolete EBS snapshots,
and Amazon S3 standard storage), or database service usage (such as RDS open-source engines,
Graviton adoption, and On-demand coverage). These benchmarks and KPIs can help you verify that
you use AWS services in the most cost-effective manner.
The following table provides a list of standard AWS metrics for reference. Each organization can
have different target values for these KPIs.
Category KPI (%) Description
