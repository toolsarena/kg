---
title: "4. Enable X-Ray Insights:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 210
---

# 4. Enable X-Ray Insights:

a. Turn on X-Ray Insights for automated anomaly detection in traces.
b. Examine insights to pinpoint patterns and ascertain root causes, such as increased fault rates
or latencies.
c. Consult the insights timeline for a chronological analysis of detected issues.
5. Use X-Ray Analytics: X-Ray Analytics allows you to thoroughly explore trace data, pinpoint
patterns, and extract insights.
6. Use groups in X-Ray: Create groups in X-Ray to filter traces based on criteria such as high
latency, allowing for more targeted analysis.
7. Incorporate Amazon DevOps Guru: Engage Amazon DevOps Guru to benefit from machine
learning models pinpointing operational anomalies in traces.
8. Use CloudWatch Synthetics: Use CloudWatch Synthetics to create canaries for continually
monitoring your endpoints and workflows. These canaries can integrate with X-Ray to provide
trace data for in-depth analysis of the applications being tested.
9. Use Real User Monitoring (RUM): With AWS X-Ray and CloudWatch RUM, you can analyze and
debug the request path starting from end users of your application through downstream AWS
managed services. This helps you identify latency trends and errors that impact your end users.
10.Correlate with logs: Correlate trace data with related logs within the X-Ray trace view for
a granular perspective on application behavior. This allows you to view log events directly
associated with traced transactions.
11.Implement CloudWatch cross-account observability: Monitor and troubleshoot applications
that span multiple accounts within a Region.
