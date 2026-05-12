---
title: "Benefits of establishing this best practice:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 598
---

# Benefits of establishing this best practice:

• Increased consistency across environments: Since there are no differences in infrastructure
resources across environments, consistency is increased and testing is simplified.
• Reduction in configuration drifts: By replacing infrastructure resources with a known and
version-controlled configuration, the infrastructure is set to a known, tested, and trusted state,
avoiding configuration drifts.
• Reliable atomic deployments: Deployments either complete successfully or nothing changes,
increasing consistency and reliability in the deployment process.
• Simplified deployments: Deployments are simplified because they don't need to support
upgrades. Upgrades are just new deployments.
• Safer deployments with fast rollback and recovery processes: Deployments are safer because
the previous working version is not changed. You can roll back to it if errors are detected.
• Enhanced security posture: By not allowing changes to infrastructure, remote access
mechanisms (such as SSH) can be disabled. This reduces the attack vector, improving your
organization's security posture.
