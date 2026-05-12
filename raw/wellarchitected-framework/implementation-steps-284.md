---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 207
---

# Implementation steps

1. Set up CloudWatch Logs: Configure applications and services to send logs to CloudWatch Logs.
2. Use log anomaly detection: Utilize Amazon CloudWatch Logs anomaly detection to
automatically identify and alert on unusual log patterns. This tool helps you proactively manage
anomalies in your logs and detect potential issues early.
3. Set up CloudWatch Logs Insights: Use CloudWatch Logs Insights to interactively search and
analyze your log data.
a. Craft queries to extract patterns, visualize log data, and derive actionable insights.
b. Use CloudWatch Logs Insights pattern analysis to analyze and visualize frequent log patterns.
This feature helps you understand common operational trends and potential outliers in your
log data.
c. Use CloudWatch Logs compare (diff) to perform differential analysis between different time
periods or across different log groups. Use this capability to pinpoint changes and assess their
impacts on your system's performance or behavior.
