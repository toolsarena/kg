---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 615
---

# Implementation guidance

Testing backup and restore capability increases confidence in the ability to perform these
actions during an outage. Periodically restore backups to a new location and run tests to verify
the integrity of the data. Some common tests that should be performed are checking if all
data is available, is not corrupted, is accessible, and that any data loss falls within the RPO for
the workload. Such tests can also help ascertain if recovery mechanisms are fast enough to
accommodate the workload's RTO.


# Implementation guidance

Deploy and operate all production workloads in at least two Availability Zones (AZs) in a Region.