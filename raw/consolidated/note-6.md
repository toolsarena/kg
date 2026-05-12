---
title: "Note"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 672
---

# Note

For every experiment, clearly understand the scope and its impact. We recommend
that faults should be simulated first on a non-production environment before being
run in production.
Experiments should run in production under real-world load using canary deployments
that spin up both a control and experimental system deployment, where feasible. Running
experiments during off-peak times is a good practice to mitigate potential impact when first
experimenting in production. Also, if using actual customer traffic poses too much risk, you
can run experiments using synthetic traffic on production infrastructure against the control
and experimental deployments. When using production is not possible, run experiments in
pre-production environments that are as close to production as possible.
You must establish and monitor guardrails to ensure the experiment does not impact
production traffic or other systems beyond acceptable limits. Establish stop conditions
to stop an experiment if it reaches a threshold on a guardrail metric that you define. This
should include the metrics for steady state for the workload, as well as the metric against the
components into which you’re injecting the fault. A synthetic monitor (also known as a user
canary) is one metric you should usually include as a user proxy. Stop conditions for AWS FIS
