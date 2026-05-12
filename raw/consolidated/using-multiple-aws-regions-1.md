---
title: "Using multiple AWS Regions"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 621
---

# Using multiple AWS Regions

If you have workloads that require extreme resilience (such as critical infrastructure, health-related
applications, or services with stringent customer or mandated availability requirements), you may
require additional availability beyond what a single AWS Region can provide. In this case, you
should deploy and operate your workload across at least two AWS Regions (assuming that your
data residency requirements allow it).
AWS Regions are located in different geographical regions around the world and in multiple
continents. AWS Regions have even greater physical separation and isolation than Availability
