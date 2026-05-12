---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 263
---

# Common anti-patterns:

• You suffered an extended outage because your organization commonly uses buggy library. You
have since migrated to a reliable library. The other teams in your organization do not know they
are at risk. No one documents and shares the experience with this library, and they are not aware
of the risk.
• You have identified an edge case in an internally-shared microservice that causes sessions to
drop. You have updated your calls to the service to avoid this edge case. The other teams in your
organization do not know that they are at risk.
• You have found a way to significantly reduce the CPU utilization requirements for one of your
microservices. You do not know if any other teams could take advantage of this technique.
Benefits of establishing this best practice: Share lessons learned to support improvement and to
maximize the benefits of experience.
Level of risk exposed if this best practice is not established: Low
