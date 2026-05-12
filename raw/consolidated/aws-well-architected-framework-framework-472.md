---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 616
---

# AWS Well-Architected Framework Framework

Using AWS, you can stand up a testing environment and restore your backups to assess RTO and
RPO capabilities, and run tests on data content and integrity.
Additionally, Amazon RDS and Amazon DynamoDB allow point-in-time recovery (PITR). Using
continuous backup, you can restore your dataset to the state it was in at a specified date and time.
If all the data is available, is not corrupted, is accessible, and any data loss falls within the RPO
for the workload. Such tests can also help ascertain if recovery mechanisms are fast enough to
accommodate the workload's RTO.
AWS Elastic Disaster Recovery offers continual point-in-time recovery snapshots of Amazon EBS
volumes. As source servers are replicated, point-in-time states are chronicled over time based on
the configured policy. Elastic Disaster Recovery helps you verify the integrity of these snapshots by
launching instances for test and drill purposes without redirecting the traffic.
