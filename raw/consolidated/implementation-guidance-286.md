---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 975
---

# Implementation guidance

If you have multiple users or applications accessing the same datasets, using shared storage
technology is crucial to use efficient infrastructure for your workload. Shared storage technology
provides a central location to store and manage datasets and avoid data duplication. It also
enforces consistency of the data across different systems. Moreover, shared storage technology
allows for more efficient use of compute power, as multiple compute resources can access and
process data at the same time in parallel.
Fetch data from these shared storage services only as needed and detach unused volumes to free
up resources.


# Implementation guidance

Moving data around your organization requires compute, networking, and storage resources. Use
techniques to minimize data movement and improve the overall efficiency of your workload.