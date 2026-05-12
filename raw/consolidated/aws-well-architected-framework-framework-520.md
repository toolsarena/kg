---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 673
---

# AWS Well-Architected Framework Framework

are supported as part of the experiment template, allowing up to five stop-conditions per
template.
One of the principles of chaos is minimize the scope of the experiment and its impact:
While there must be an allowance for some short-term negative impact, it is the responsibility
and obligation of the Chaos Engineer to ensure the fallout from experiments are minimized
and contained.
A method to verify the scope and potential impact is to perform the experiment in a non-
production environment first, verifying that thresholds for stop conditions activate as
expected during an experiment and observability is in place to catch an exception, instead of
directly experimenting in production.
When running fault injection experiments, verify that all responsible parties are well-
informed. Communicate with appropriate teams such as the operations teams, service
reliability teams, and customer support to let them know when experiments will be run
and what to expect. Give these teams communication tools to inform those running the
experiment if they see any adverse effects.
You must restore the workload and its underlying systems back to the original known-good
state. Often, the resilient design of the workload will self-heal. But some fault designs or
failed experiments can leave your workload in an unexpected failed state. By the end of
the experiment, you must be aware of this and restore the workload and systems. With
AWS FIS you can set a rollback configuration (also called a post action) within the action
parameters. A post action returns the target to the state that it was in before the action was
run. Whether automated (such as using AWS FIS) or manual, these post actions should be part
of a playbook that describes how to detect and handle failures.
d. Verify the hypothesis.
Principles of Chaos Engineering gives this guidance on how to verify steady state of your
workload:
Focus on the measurable output of a system, rather than internal attributes of the system.
Measurements of that output over a short period of time constitute a proxy for the system’s
steady state. The overall system’s throughput, error rates, and latency percentiles could all
be metrics of interest representing steady state behavior. By focusing on systemic behavior
patterns during experiments, chaos engineering verifies that the system does work, rather
than trying to validate how it works.
