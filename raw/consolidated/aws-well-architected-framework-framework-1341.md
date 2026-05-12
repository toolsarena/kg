---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 778
---

# AWS Well-Architected Framework Framework

• Use cross-zone turned on for increased availability and flexibility. By default, cross-zone is
turned on for ALB and in NLB you can turn it on per target group.
• Turn on HTTP keep-alives for your HTTP workloads (only ALB). With this feature, the load
balancer can reuse backend connections until the keep-alive timeout expires, improving your
HTTP request and response time and also reducing resource utilization on your backend targets.
For detail on how to do this for Apache and Nginx, see What are the optimal settings for using
Apache or NGINX as a backend server for ELB?
• Turn on monitoring for your load balancer.
• Turn on access logs for your Application Load Balancer and Network Load Balancer.
• The main fields to consider for ALB
are request_processing_time, request_processing_time,
and response_processing_time.
• The main fields to consider for NLB are connection_time and tls_handshake_time.
• Be ready to query the logs when you need them. You can use Amazon Athena to query
both ALB logs and NLB logs.
• Create alarms for performance related metrics such as TargetResponseTime for ALB.


# AWS Well-Architected Framework Framework

• AWS re:Invent 2018: Elastic Load Balancing: Deep Dive and Best Practices
• AWS re:Invent 2021 - How to choose the right load balancer for your AWS workloads
• AWS re:Invent 2019: Get the most from Elastic Load Balancing for different workloads

# AWS Well-Architected Framework Framework

A primary consideration for improving your workload’s performance is to understand the latency
and throughput requirements, and then choose network protocols that optimize performance.