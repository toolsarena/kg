---
title: "General guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 521
---

# General guidance

• Make sure that the performance and reliability service-level objectives (SLOs) that your
dependencies offer meet the performance and reliability requirements of your workload.
• Use AWS observability services to monitor response times and error rates to make sure your
dependency is providing service at the levels needed by your workload.
• Identify the potential challenges that your workload may face when communicating with its
dependencies. Distributed systems come with a wide range of challenges that might increase
architectural complexity, operational burden, and cost. Common challenges include latency,
network disruptions, data loss, scaling, and data replication lag.
• Implement robust error handling and logging to help you troubleshoot problems when your
dependency experiences issues.
