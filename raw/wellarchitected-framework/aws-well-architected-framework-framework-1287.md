---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 697
---

# AWS Well-Architected Framework Framework

is maintained. Therefore, the former read/write instance in the primary Region will become a
replica and receive updates from the recovery Region.
In cases where this is not automatic, you will need to re-establish the database in the primary
Region as a replica of the database in the recovery Region. In many cases this will involve
deleting the old primary database, and creating new replicas.
After a failover, if you can continue running in your recovery Region, consider making this the
new primary Region. You would still do all the above steps to make the former primary Region
into a recovery Region. Some organizations do a scheduled rotation, swapping their primary and
recovery Regions periodically (for example every three months).
All of the steps required to fail over and fail back should be maintained in a playbook that is
available to all members of the team, and is periodically reviewed.
When using Elastic Disaster Recovery, the service will assist in orchestrating and automating the
failback process. For more details, see Performing a failback.
