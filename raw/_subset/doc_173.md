---
title: "AWS IoT Greengrass Use to run local compute, messaging, and"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 785
---

# AWS IoT Greengrass Use to run local compute, messaging, and

data caching for connected devices.
• Some applications require fixed entry points or higher performance by reducing first byte latency
and jitter, and increasing throughput. These applications can benefit from networking services
that provide static anycast IP addresses and TCP termination at edge locations. AWS Global
Accelerator can improve performance for your applications by up to 60% and provide quick
failover for multi-region architectures. AWS Global Accelerator provides you with static anycast
IP addresses that serve as a fixed entry point for your applications hosted in one or more AWS
Regions. These IP addresses permit traffic to ingress onto the AWS global network as close to
your users as possible. AWS Global Accelerator reduces the initial connection setup time by
establishing a TCP connection between the client and the AWS edge location closest to the
client. Review the use of AWS Global Accelerator to improve the performance of your TCP/UDP
workloads and provide quick failover for multi-Region architectures.
