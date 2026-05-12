---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 378
---

# Implementation guidance

To harden your systems, start from the latest versions of operating systems, container images,
and application libraries. Apply patches to known issues. Minimize the system by removing any
unneeded applications, services, device drivers, default users, and other credentials. Take any other
needed actions, such as disabling ports to create an environment that has only the resources and
capabilities needed by your workloads. From this baseline, you can then install software, agents, or
other processes you need for purposes such as workload monitoring or vulnerability management.
You can reduce the burden of hardening systems by using guidance that trusted sources provide,
such as the Center for Internet Security (CIS) and the Defense Information Systems Agency (DISA)
Security Technical Implementation Guides (STIGs). We recommend you start with an Amazon
Machine Image (AMI) published by AWS or an APN partner, and use the AWS EC2 Image Builder to
automate configuration according to an appropriate combination of CIS and STIG controls.
While there are available hardened images and EC2 Image Builder recipes that apply the CIS
or DISA STIG recommendations, you may find their configuration prevents your software from
running successfully. In this situation, you can start from a non-hardened base image, install your
