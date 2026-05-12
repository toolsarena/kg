---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 205
---

# Implementation steps

1. Analyze and review: Regularly review and interpret your workload metrics.
a. Prioritize business outcome metrics over purely technical metrics.
b. Understand the significance of spikes, drops, or patterns in your data.
2. Utilize Amazon CloudWatch: Use Amazon CloudWatch for a centralized view and deep-dive
analysis.
a. Configure CloudWatch dashboards to visualize your metrics and compare them over time.
b. Use percentiles in CloudWatch to get a clear view of metric distribution, which can help in
defining SLAs and understanding outliers.
c. Set up CloudWatch anomaly detection to identify unusual patterns without relying on static
thresholds.
d. Implement CloudWatch cross-account observability to monitor and troubleshoot applications
that span multiple accounts within a Region.
e. Use CloudWatch Metric Insights to query and analyze metric data across accounts and
Regions, identifying trends and anomalies.
f. Apply CloudWatch Metric Math to transform, aggregate, or perform calculations on your
metrics for deeper insights.
3. Employ Amazon DevOps Guru: Incorporate Amazon DevOps Guru for its machine learning-
enhanced anomaly detection to identify early signs of operational issues for your serverless
applications and remediate them before they impact your customers.
4. Optimize based on insights: Make informed decisions based on your metric analysis to adjust
and improve your workloads.
