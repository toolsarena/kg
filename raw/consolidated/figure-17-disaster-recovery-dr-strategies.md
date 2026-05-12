---
title: "Figure 17: Disaster recovery (DR) strategies"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 686
---

# Figure 17: Disaster recovery (DR) strategies

• Backup and restore (RPO in hours, RTO in 24 hours or less): Back up your data and applications
into the recovery Region. Using automated or continuous backups will permit point in time
recovery (PITR), which can lower RPO to as low as 5 minutes in some cases. In the event of a
disaster, you will deploy your infrastructure (using infrastructure as code to reduce RTO), deploy
your code, and restore the backed-up data to recover from a disaster in the recovery Region.
• Pilot light (RPO in minutes, RTO in tens of minutes): Provision a copy of your core workload
infrastructure in the recovery Region. Replicate your data into the recovery Region and create
backups of it there. Resources required to support data replication and backup, such as
databases and object storage, are always on. Other elements such as application servers or
serverless compute are not deployed, but can be created when needed with the necessary
configuration and application code.
• Warm standby (RPO in seconds, RTO in minutes): Maintain a scaled-down but fully functional
version of your workload always running in the recovery Region. Business-critical systems are
fully duplicated and are always on, but with a scaled down fleet. Data is replicated and live in the
recovery Region. When the time comes for recovery, the system is scaled up quickly to handle
the production load. The more scaled-up the warm standby is, the lower RTO and control plane
reliance will be. When fully scales this is known as hot standby.
• Multi-Region (multi-site) active-active (RPO near zero, RTO potentially zero): Your workload is
deployed to, and actively serving traffic from, multiple AWS Regions. This strategy requires you


# Figure 19: Backup and restore architecture

For more details on this strategy see Disaster Recovery (DR) Architecture on AWS, Part II: Backup
and Restore with Rapid Recovery.

# Figure 19: Backup and restore architecture

For more details on this strategy see Disaster Recovery (DR) Architecture on AWS, Part II: Backup
and Restore with Rapid Recovery.

# Figure 20: Pilot light architecture

For more details on this strategy, see Disaster Recovery (DR) Architecture on AWS, Part III: Pilot
Light and Warm Standby.

# Figure 20: Pilot light architecture

For more details on this strategy, see Disaster Recovery (DR) Architecture on AWS, Part III: Pilot
Light and Warm Standby.