---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 937
---

# Implementation guidance

The cloud provides the flexibility to expand or reduce your resources dynamically through a variety
of mechanisms to meet changes in demand. Optimally matching supply to demand delivers the
lowest environmental impact for a workload.
Demand can be fixed or variable, requiring metrics and automation to make sure that management
does not become burdensome. Applications can scale vertically (up or down) by modifying the
instance size, horizontally (in or out) by modifying the number of instances, or a combination of
both.
You can use a number of different approaches to match supply of resources with demand.
• Target-tracking approach: Monitor your scaling metric and automatically increase or decrease
capacity as you need it.
• Predictive scaling: Scale in anticipation of daily and weekly trends.
• Schedule-based approach: Set your own scaling schedule according to predictable load changes.
• Service scaling: Pick services (like serverless) that are natively scaling by design or provide auto
scaling as a feature.
Identify periods of low or no utilization and scale resources to remove excess capacity and improve
efficiency.
