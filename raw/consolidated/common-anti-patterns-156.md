---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 637
---

# Common anti-patterns:

• Planning for failure is not part of the planning and design phase.
• RTO and RPO are not established.
• Insufficient monitoring to detect failing resources.
• Proper isolation of failure domains.
• Multi-Region fail over is not considered.
• Detection for failure is too sensitive or aggressive when deciding to failover.
• Not testing or validating failover design.
• Performing auto healing automation, but not notifying that healing was needed.
• Lack of dampening period to avoid failing back too soon.
Benefits of establishing this best practice: You can build more resilient systems that maintain
reliability when experiencing failures by degrading gracefully and recovering quickly.
Level of risk exposed if this best practice is not established: High


# Common anti-patterns:

• Provisioning resources without autoscaling.
• Deploying applications in instances or containers individually.
• Deploying applications that cannot be deployed into multiple locations without using automatic
recovery.