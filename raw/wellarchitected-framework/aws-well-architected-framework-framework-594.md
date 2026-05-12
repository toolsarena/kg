---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 784
---

# AWS Well-Architected Framework Framework

• Where your data is located: For data-heavy applications (such as big data and machine
learning), application code should run as close to the data as possible.
• Where your users are located: For user-facing applications, choose a Region (or Regions) close
to your workload’s users.
• Other constraints: Consider constraints such as cost and compliance as explained in What to
Consider when Selecting a Region for your Workloads.
• Use AWS Local Zones to run workloads like video rendering. Local Zones allow you to benefit
from having compute and storage resources closer to end users.
• Use AWS Outposts for workloads that need to remain on-premises and where you want that
workload to run seamlessly with the rest of your other workloads in AWS.
• Applications like high-resolution live video streaming, high-fidelity audio, and augmented
reality or virtual reality (AR/VR) require ultra-low-latency for 5G devices. For such applications,
consider AWS Wavelength. AWS Wavelength embeds AWS compute and storage services within
5G networks, providing mobile edge computing infrastructure for developing, deploying, and
scaling ultra-low-latency applications.
• Use local caching or AWS Caching Solutions for frequently used assets to improve performance,
reduce data movement, and lower environmental impact.
