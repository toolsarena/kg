---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 128
---

# Implementation steps

1. Work with leadership across your organization to support experimentation. Team members
should be encouraged to conduct experiments in a safe manner.
2. Provide your team members with an environment where they can safely experiment. They must
have access to an environment that is like production.
a. You can use a separate AWS account to create a sandbox environment for experimentation.
AWS Control Tower can be used to provision these accounts.
3. Use feature flags and A/B testing to experiment safely and gather user feedback.
a. AWS AppConfig Feature Flags provides the ability to create feature flags.
b. You can use AWS Lambda versions to deploy a new version of a function for beta testing.
Level of effort for the implementation plan: High. Providing team members with an environment
to experiment in and a safe way to conduct experiments can require significant investment. You
may also need to modify application code to use feature flags or support A/B testing.


# Implementation steps

1. Determine whether the workload component is suitable for automatic scaling.
2. Determine what kind of scaling mechanism is most appropriate for the workload: metric-based
scaling, scheduled scaling, or predictive scaling.