---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 579
---

# Implementation steps

• Use AWS X-Ray on all supported native services like Amazon S3, AWS Lambda, and Amazon API
Gateway. These AWS services enable X-Ray with configuration toggles using infrastructure as
code, AWS SDKs, or the AWS Management Console.
• Instrument applications AWS Distro for Open Telemetry and X-Ray or third-party collection
agents.
• Review the AWS X-Ray Developer Guide for programming language specific implementation.
These documentation sections detail how to instrument HTTP requests, SQL queries, and other
processes specific to your application programming language.
• Use X-Ray tracing for Amazon CloudWatch Synthetic Canaries and Amazon CloudWatch
RUM to analyze the request path from your end user client through your downstream AWS
infrastructure.
• Configure CloudWatch metrics and alarms based on resource health and canary telemetry so
that teams are alerted to issues quickly, and can then deep dive into traces and service maps
with ServiceLens.
• Enable X-Ray integration for third party tracing tools like Datadog, New Relic, or Dynatrace if you
are using third party tools for your primary tracing solution.
