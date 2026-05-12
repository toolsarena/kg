---
title: "Networking and content delivery 764"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 769
---

# Networking and content delivery 764

| Improvement opportunity | Solution |
| --- | --- |
|  | Amazon CloudFront can improve the
performance of your workload content
delivery and latency globally.
Use Lambda@edge to run functions that
customize the content that CloudFront
delivers closer to the users, reduce latency,
and improve performance.
Amazon Route 53 offers latency-based
routing, geolocation routing, geoproximity
routing, and IP-based routing options to
help you improve your workload’s performan
ce for a global audience. Identify which
routing option would optimize your workload
performance by reviewing your workload
traffic and user location when your workload
is distributed globally. |
| Storage resource features | Amazon S3 Transfer Acceleration is a feature
that lets external users benefit from the
networking optimizations of CloudFront to
upload data to Amazon S3. This improves the
ability to transfer large amounts of data from
remote locations that don’t have dedicated
connectivity to the AWS Cloud.
Amazon S3 Multi-Region Access Points
replicates content to multiple Regions and
simplifies the workload by providing one
access point. When a Multi-Region Access
Point is used, you can request or write data
to Amazon S3 with the service identifying the
lowest latency bucket. |
