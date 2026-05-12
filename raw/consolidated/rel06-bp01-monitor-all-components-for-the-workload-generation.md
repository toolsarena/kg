---
title: "REL06-BP01 Monitor all components for the workload (Generation)"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 559
---

# REL06-BP01 Monitor all components for the workload (Generation)

Monitor the components of the workload with Amazon CloudWatch or third-party tools. Monitor
AWS services with AWS Health Dashboard.
All components of your workload should be monitored, including the front-end, business logic,
and storage tiers. Define key metrics, describe how to extract them from logs (if necessary), and
set thresholds for invoking corresponding alarm events. Ensure metrics are relevant to the key
performance indicators (KPIs) of your workload, and use metrics and logs to identify early warning
signs of service degradation. For example, a metric related to business outcomes such as the
number of orders successfully processed per minute, can indicate workload issues faster than
technical metric, such as CPU Utilization. Use AWS Health Dashboard for a personalized view into
the performance and availability of the AWS services underlying your AWS resources.
Monitoring in the cloud offers new opportunities. Most cloud providers have developed
customizable hooks and can deliver insights to help you monitor multiple layers of your workload.
AWS services such as Amazon CloudWatch apply statistical and machine learning algorithms
to continually analyze metrics of systems and applications, determine normal baselines, and
surface anomalies with minimal user intervention. Anomaly detection algorithms account for the
seasonality and trend changes of metrics.


# REL06-BP02 Define and calculate metrics (Aggregation)

Collect metrics and logs from your workload components and calculate relevant aggregate
metrics from them. These metrics provide broad and deep observability of your workload and can
significantly improve your resilience posture.

# REL06-BP02 Define and calculate metrics (Aggregation)

Collect metrics and logs from your workload components and calculate relevant aggregate
metrics from them. These metrics provide broad and deep observability of your workload and can
significantly improve your resilience posture.