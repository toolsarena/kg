---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 216
---

# AWS Well-Architected Framework Framework

2. Use Markdown widgets: Before diving into the metrics, use Markdown widgets to add textual
context at the top of your dashboard. This should explain what the dashboard covers, the
significance of the represented metrics, and can also contain links to other dashboards and
troubleshooting tools.
3. Create dashboard variables: Incorporate dashboard variables where appropriate to allow for
dynamic and flexible dashboard views.
4. Create metrics widgets: Add metric widgets to visualize various metrics your application emits,
tailoring these widgets to effectively represent system health and business outcomes.
5. Log Insights queries: Utilize CloudWatch Log Insights to derive actionable metrics from your
logs and display these insights on your dashboard.
6. Set up alarms: Integrate CloudWatch Alarms into your dashboard for a quick view of any metrics
breaching their thresholds.
7. Use Contributor Insights: Incorporate CloudWatch Contributor Insights to analyze high-
cardinality fields and get a clearer understanding of your resource's top contributors.
8. Design custom widgets: For specific needs not met by standard widgets, consider creating
custom widgets. These can pull from various data sources or represent data in unique ways.
9. Use AWS Health: AWS Health is the authoritative source of information about the health of your
AWS Cloud resources. Use AWS Health Dashboard out of the box, or use AWS Health data in
your own dashboards and tools so you have the right information available to make informed
decisions.
10.Iterate and refine: As your application evolves, regularly revisit your dashboard to ensure its
relevance.
