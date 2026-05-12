---
title: "Best practices"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 605
---

# Best practices

• REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data
from sources
• REL09-BP02 Secure and encrypt backups
• REL09-BP03 Perform data backup automatically
• REL09-BP04 Perform periodic recovery of the data to verify backup integrity and processes
REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the data
from sources
Understand and use the backup capabilities of the data services and resources used by the
workload. Most services provide capabilities to back up workload data.
Desired outcome: Data sources have been identified and classified based on criticality. Then,
establish a strategy for data recovery based on the RPO. This strategy involves either backing up
these data sources, or having the ability to reproduce data from other sources. In the case of data
loss, the strategy implemented allows recovery or the reproduction of data within the defined RPO
and RTO.


# Best practices

• REL10-BP01 Deploy the workload to multiple locations
• REL10-BP02 Automate recovery for components constrained to a single location
• REL10-BP03 Use bulkhead architectures to limit scope of impact

# Best practices

• REL11-BP01 Monitor all components of the workload to detect failures
• REL11-BP02 Fail over to healthy resources
• REL11-BP03 Automate healing on all layers
• REL11-BP04 Rely on the data plane and not the control plane during recovery

# Best practices

• REL12-BP01 Use playbooks to investigate failures
• REL12-BP02 Perform post-incident analysis
• REL12-BP03 Test scalability and performance requirements
• REL12-BP04 Test resiliency using chaos engineering
• REL12-BP05 Conduct game days regularly