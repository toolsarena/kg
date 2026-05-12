---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 781
---

# AWS Well-Architected Framework Framework

lower latency between your client devices and your workload on AWS. With AWS Transfer
Family, you can use TCP-based protocols such as Secure Shell File Transfer Protocol (SFTP) and
File Transfer Protocol over SSL (FTPS) to securely scale and manage your file transfers to AWS
storage services.
• Use network latency to determine if TCP is appropriate for communication between workload
components. If the network latency between your client application and server is high, then
the TCP three-way handshake can take some time, thereby impacting on the responsiveness
of your application. Metrics such as time to first byte (TTFB) and round-trip time (RTT) can be
used to measure network latency. If your workload serves dynamic content to users, consider
using Amazon CloudFront, which establishes a persistent connection to each origin for dynamic
content to remove the connection setup time that would otherwise slow down each client
request.
• Using TLS with TCP or UDP can result in increased latency and reduced throughput for your
workload due to the impact of encryption and decryption. For such workloads, consider SSL/
TLS offloading on Elastic Load Balancing to improve workload performance by allowing the
load balancer to handle SSL/TLS encryption and decryption process instead of having backend
instances do it. This can help reduce the CPU utilization on the backend instances, which can
improve performance and increase capacity.
• Use the Network Load Balancer (NLB) to deploy services that rely on the UDP protocol, such
as authentication and authorization, logging, DNS, IoT, and streaming media, to improve the
performance and reliability of your workload. The NLB distributes incoming UDP traffic across
multiple targets, allowing you to scale your workload horizontally, increase capacity, and reduce
the overhead of a single target.
• For your High Performance Computing (HPC) workloads, consider using the Elastic Network
Adapter (ENA) Express functionality that uses the SRD protocol to improve network performance
by providing a higher single flow bandwidth (25 Gbps) and lower tail latency (99.9 percentile) for
network traffic between EC2 instances.
• Use the Application Load Balancer (ALB) to route and load balance your gRPC (Remote Procedure
Calls) traffic between workload components or between gRPC clients and services. gRPC uses the
TCP-based HTTP/2 protocol for transport and it provides performance benefits such as lighter
network footprint, compression, efficient binary serialization, support for numerous languages,
and bi-directional streaming.
