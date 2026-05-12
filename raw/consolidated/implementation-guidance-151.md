---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 567
---

# Implementation guidance

Workloads should be equipped with real-time processing and alarming to improve the detectability
of issues that could impact the availability of the application and serve as triggers for automated
response. Organizations can perform real-time processing and alarming by creating alerts with
defined metrics in order to receive notifications whenever significant events occur or a metric
exceeds a threshold.
Amazon CloudWatch allows you to create metric and composite alarms using CloudWatch
alarms based on static threshold, anomaly detection, and other criteria. For more detail on the
types of alarms you can configure using CloudWatch, see the alarms section of the CloudWatch
documentation.
