---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 148
---

# AWS Well-Architected Framework Framework

1. Adopt AWS X-Ray: Integrate X-Ray into your application to gain insights into its behavior,
understand its performance, and pinpoint bottlenecks. Utilize X-Ray Insights for automatic trace
analysis.
2. Instrument your services: Verify that every service, from an AWS Lambda function to an EC2
instance, sends trace data. The more services you instrument, the clearer the end-to-end view.
3. Incorporate CloudWatch Real User Monitoring and synthetic monitoring: Integrate Real User
Monitoring (RUM) and synthetic monitoring with X-Ray. This allows for capturing real-world user
experiences and simulating user interactions to identify potential issues.
4. Use the CloudWatch agent: The agent can send traces from either X-Ray or OpenTelemetry,
enhancing the depth of insights obtained.
5. Use Amazon DevOps Guru: DevOps Guru uses data from X-Ray, CloudWatch, AWS Config, and
AWS CloudTrail to provide actionable recommendations.
6. Analyze traces: Regularly review the trace data to discern patterns, anomalies, or bottlenecks
that might impact your application's performance.
7. Set up alerts: Configure alarms in CloudWatch for unusual patterns or extended latencies,
allowing proactive issue addressing.
8. Continuous improvement: Revisit your tracing strategy as services are added or modified to
capture all relevant data points.
