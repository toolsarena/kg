---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 777
---

# Implementation steps

• Define your load balancing requirements including traffic volume, availability and application
scalability.
• Choose the right load balancer type for your application.
• Use Application Load Balancer for HTTP/HTTPS workloads.
• Use Network Load Balancer for non-HTTP workloads that run on TCP or UDP.
• Use a combination of both (ALB as a target of NLB) if you want to leverage features of both
products. For example, you can do this if you want to use the static IPs of NLB together with
HTTP header based routing from ALB, or if you want to expose your HTTP workload to an AWS
PrivateLink.
• For a full comparison of load balancers, see ELB product comparison.
• Use SSL/TLS offloading if possible.
• Configure HTTPS/TLS listeners with both Application Load Balancer and Network Load
Balancer integrated with AWS Certificate Manager.
• Note that some workloads may require end-to-end encryption for compliance reasons. In this
case, it is a requirement to allow encryption at the targets.
• For security best practices, see SEC09-BP02 Enforce encryption in transit.
• Select the right routing algorithm (only ALB).
• The routing algorithm can make a difference in how well-used your backend targets are and
therefore how they impact performance. For example, ALB provides two options for routing
algorithms:
• Least outstanding requests: Use to achieve a better load distribution to your backend targets
for cases when the requests for your application vary in complexity or your targets vary in
processing capability.
• Round robin: Use when the requests and targets are similar, or if you need to distribute
requests equally among targets.
• Consider cross-zone or zonal isolation.
• Use cross-zone turned off (zonal isolation) for latency improvements and zonal failure
domains. It is turned off by default in NLB and in ALB you can turn it off per target group.


# Implementation steps

• Use the AWS Global Accelerator and AWS Transfer Family services to improve the throughput
of your online file transfer applications. The AWS Global Accelerator service helps you achieve