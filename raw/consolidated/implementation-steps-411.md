---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 756
---

# Implementation steps

• Identify the key performance metrics for your data store to track.
• Amazon S3 Metrics and dimensions
• Monitoring metrics for in an Amazon RDS instance
• Monitoring DB load with Performance Insights on Amazon RDS
• Overview of Enhanced Monitoring
• DynamoDB Metrics and dimensions
• Monitoring DynamoDB Accelerator
• Monitoring Amazon MemoryDB with Amazon CloudWatch
• Which Metrics Should I Monitor?
• Monitoring Amazon Redshift cluster performance
• Timestream metrics and dimensions
• Amazon CloudWatch metrics for Amazon Aurora
• Logging and monitoring in Amazon Keyspaces (for Apache Cassandra)
• Monitoring Amazon Neptune Resources
• Use an approved logging and monitoring solution to collect these metrics. Amazon CloudWatch
can collect metrics across the resources in your architecture. You can also collect and publish
custom metrics to surface business or derived metrics. Use CloudWatch or third-party solutions
to set alarms that indicate when thresholds are breached.
• Check if data store monitoring can benefit from a machine learning solution that detects
performance anomalies.
• Amazon DevOps Guru for Amazon RDS provides visibility into performance issues and makes
recommendations for corrective actions.
