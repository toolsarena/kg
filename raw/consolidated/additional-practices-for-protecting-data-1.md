---
title: "Additional practices for protecting data"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 693
---

# Additional practices for protecting data

With all strategies, you must also mitigate against a data disaster. Continuous data replication
protects you against some types of disaster, but it may not protect you against data corruption
or destruction unless your strategy also includes versioning of stored data or options for point-
in-time recovery. You must also back up the replicated data in the recovery site to create point-
in-time backups in addition to the replicas.
