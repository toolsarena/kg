---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 644
---

# Common anti-patterns:

• Dependence on changing DNS records to re-route traffic.
• Dependence on control-plane scaling operations to replace impaired components due to
insufficiently provisioned resources.
• Relying on extensive, multi service, multi-API control plane actions to remediate any category of
impairment.
Benefits of establishing this best practice: Increased success rate for automated remediation can
reduce your mean time to recovery and improve availability of the workload.
Level of risk exposed if this best practice is not established: Medium: For certain types of service
degradations, control planes are affected. Dependencies on extensive use of the control plane for
remediation may increase recovery time (RTO) and mean time to recovery (MTTR).
