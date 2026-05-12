---
title: "REL11-BP03 Automate healing on all layers"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 640
---

# REL11-BP03 Automate healing on all layers

Upon detection of a failure, use automated capabilities to perform actions to remediate.
Degradations may be automatically healed through internal service mechanisms or require
resources to be restarted or removed through remediation actions.
For self-managed applications and cross-Region healing, recovery designs and automated healing
processes can be pulled from existing best practices.
The ability to restart or remove a resource is an important tool to remediate failures. A best
practice is to make services stateless where possible. This prevents loss of data or availability
on resource restart. In the cloud, you can (and generally should) replace the entire resource (for
example, a compute instance or serverless function) as part of the restart. The restart itself is a
simple and reliable way to recover from failure. Many different types of failures occur in workloads.
Failures can occur in hardware, software, communications, and operations.
Restarting or retrying also applies to network requests. Apply the same recovery approach to both
a network timeout and a dependency failure where the dependency returns an error. Both events
have a similar effect on the system, so rather than attempting to make either event a special
case, apply a similar strategy of limited retry with exponential backoff and jitter. Ability to restart
is a recovery mechanism featured in recovery-oriented computing and high availability cluster
architectures.
Desired outcome: Automated actions are performed to remediate detection of a failure.
