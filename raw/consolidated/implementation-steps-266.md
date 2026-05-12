---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 139
---

# Implementation steps

1. Identify what data to collect: Ascertain the essential metrics, logs, and traces that would offer
substantial insights into your workload's health, performance, and behavior.
2. Deploy the CloudWatch agent: The CloudWatch agent is instrumental in procuring system
and application metrics and logs from your workload and its underlying infrastructure. The
CloudWatch agent can also be used to collect OpenTelemetry or X-Ray traces and send them to
X-Ray.
3. Implement anomaly detection for logs and metrics: Use CloudWatch Logs anomaly detection
and CloudWatch Metrics anomaly detection to automatically identify unusual activities in
your application's operations. These tools use machine learning algorithms to detect and alert
on anomalies, which enanhces your monitoring capabilities and speeds up response time to
potential disruptions or security threats. Set up these features to proactively manage application
health and security.
4. Secure sensitive log data: Use Amazon CloudWatch Logs data protection to mask sensitive
information within your logs. This feature helps maintain privacy and compliance through
automatic detection and masking of sensitive data before it is accessed. Implement data
masking to securely handle and protect sensitive details such as personally identifiable
information (PII).
5. Define and monitor business KPIs: Establish custom metrics that align with your business
outcomes.
6. Instrument your application with AWS X-Ray: In addition to deploying the CloudWatch agent,
it's crucial to instrument your application to emit trace data. This process can provide further
insights into your workload's behavior and performance.
7. Standardize data collection across your application: Standardize data collection practices
across your entire application. Uniformity aids in correlating and analyzing data, providing a
comprehensive view of your application's behavior.
