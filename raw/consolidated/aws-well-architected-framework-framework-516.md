---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 669
---

# AWS Well-Architected Framework Framework

Start with a coarse categorization such as high, medium, or low. To assess priority, consider
frequency of the fault and impact of failure to the overall workload.
When considering frequency of a given fault, analyze past data for this workload when available.
If not available, use data from other workloads running in a similar environment.
When considering impact of a given fault, the larger the scope of the fault, generally the larger
the impact. Also consider the workload design and purpose. For example, the ability to access
the source data stores is critical for a workload doing data transformation and analysis. In this
case, you would prioritize experiments for access faults, as well as throttled access and latency
insertion.
Post-incident analyses are a good source of data to understand both frequency and impact of
failure modes.
Use the assigned priority to determine which faults to experiment with first and the order with
which to develop new fault injection experiments.
3. For each experiment that you perform, follow the chaos engineering and continuous resilience
flywheel in the following figure.
