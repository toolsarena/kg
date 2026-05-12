---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 615
---

# Common anti-patterns:

• Restoring a backup, but not querying or retrieving any data to check that the restoration is
usable.
• Assuming that a backup exists.
• Assuming that the backup of a system is fully operational and that data can be recovered from it.
• Assuming that the time to restore or recover data from a backup falls within the RTO for the
workload.
• Assuming that the data contained on the backup falls within the RPO for the workload
• Restoring when necessary, without using a runbook or outside of an established automated
procedure.
Benefits of establishing this best practice: Testing the recovery of the backups verifies that data
can be restored when needed without having any worry that data might be missing or corrupted,
that the restoration and recovery is possible within the RTO for the workload, and any data loss
falls within the RPO for the workload.
Level of risk exposed if this best practice is not established: Medium
