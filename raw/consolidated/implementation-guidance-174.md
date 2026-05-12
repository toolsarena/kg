---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 644
---

# Implementation guidance

To limit data plane actions, assess each service for what actions are required to restore service.
Leverage Amazon Application Recovery Controller to shift the DNS traffic. These features
continually monitor your application’s ability to recover from failures and allow you to control your
application recovery across multiple AWS Regions, Availability Zones, and on premises.
Route 53 routing policies use the control plane, so do not rely on it for recovery. The Route 53 data
planes answer DNS queries and perform and evaluate health checks. They are globally distributed
and designed for a 100% availability service level agreement (SLA).
The Route 53 management APIs and consoles where you create, update, and delete Route 53
resources run on control planes that are designed to prioritize the strong consistency and durability
that you need when managing DNS. To achieve this, the control planes are located in a single
Region: US East (N. Virginia). While both systems are built to be very reliable, the control planes
