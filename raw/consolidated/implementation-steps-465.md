---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 908
---

# Implementation steps

• Identify requirements: What is the primary goal and business requirements for the planned data
transfer between source and destination? What is the expected business outcome at the end?
Gather business requirements and define expected outcome.
• Identify source and destination: What is the data source and destination for the data transfer,
such as within AWS Regions, to AWS services, or out to the internet?
• Data transfer within an AWS Region
• Data transfer between AWS Regions
• Data transfer out to the internet
• Identify data classifications: What is the data classification for this data transfer? What kind of
data is it? How big is the data? How frequently must data be transferred? Is data sensitive?
• Identify AWS services or tools to use: Which AWS services are used for this data transfer? Is it
possible to use an already-provisioned service for another workload?
• Calculate data transfer costs: Use AWS Pricing the data transfer modeling you created
previously to calculate the data transfer costs for the workload. Calculate the data transfer costs
at different usage levels, for both increases and reductions in workload usage. Where there are
multiple options for the workload architecture, calculate the cost for each option for comparison.
• Link costs to outcomes: For each data transfer cost incurred, specify the outcome that it
achieves for the workload. If it is transfer between components, it may be for decoupling, if it is
between Availability Zones it may be for redundancy.
• Create data transfer modeling: After gathering all information, create a conceptual base data
transfer modeling for multiple use cases and different workloads.
