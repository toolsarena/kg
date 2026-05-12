---
title: "Elastic Load Balancing provides integrated certificate management and SSL/TLS decryption,"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 776
---

# Elastic Load Balancing provides integrated certificate management and SSL/TLS decryption,

allowing you the flexibility to centrally manage the SSL settings of the load balancer and offload
CPU intensive work from your workload.
After choosing the right load balancer, you can start leveraging its features to reduce the amount
of effort your backend has to do to serve the traffic.
For example, using both Application Load Balancer (ALB) and Network Load Balancer (NLB), you
can perform SSL/TLS encryption offloading, which is an opportunity to avoid the CPU-intensive
TLS handshake from being completed by your targets and also to improve certificate management.
When you configure SSL/TLS offloading in your load balancer, it becomes responsible for the
encryption of the traffic from and to clients while delivering the traffic unencrypted to your
backends, freeing up your backend resources and improving the response time for the clients.
Application Load Balancer can also serve HTTP/2 traffic without needing to support it on your
targets. This simple decision can improve your application response time, as HTTP/2 uses TCP
connections more efficiently.
Your workload latency requirements should be considered when defining the architecture. As an
example, if you have a latency-sensitive application, you may decide to use Network Load Balancer,
which offers extremely low latencies. Alternatively, you may decide to bring your workload closer
to your customers by leveraging Application Load Balancer in AWS Local Zones or even AWS
Outposts.
Another consideration for latency-sensitive workloads is cross-zone load balancing. With cross-
zone load balancing, each load balancer node distributes traffic across the registered targets in all
allowed Availability Zones.
Use Auto Scaling integrated with your load balancer. One of the key aspects of a performance
efficient system has to do with right-sizing your backend resources. To do this, you can leverage
load balancer integrations for backend target resources. Using the load balancer integration with
Auto Scaling groups, targets will be added or removed from the load balancer as required in
response to incoming traffic. Load balancers can also integrate with Amazon ECS and Amazon EKS
for containerized workloads.
• Amazon ECS - Service load balancing
