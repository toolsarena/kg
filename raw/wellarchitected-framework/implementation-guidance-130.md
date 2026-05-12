---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 495
---

# Implementation guidance

At the core of building highly available network connectivity to your public endpoints is the routing
of the traffic. To verify your traffic is able to reach the endpoints, the DNS must be able to resolve
the domain names to their corresponding IP addresses. Use a highly available and scalable Domain
Name System (DNS) such as Amazon Route 53 to manage your domain’s DNS records. You can also
use health checks provided by Amazon Route 53. The health checks verify that your application is
reachable, available, and functional, and they can be set up in a way that they mimic your user’s
behavior, such as requesting a web page or a specific URL. In case of failure, Amazon Route 53
responds to DNS resolution requests and directs the traffic to only healthy endpoints. You can also
consider using Geo DNS and Latency Based Routing capabilities offered by Amazon Route 53.
To verify that your workload itself is highly available, use Elastic Load Balancing (ELB). Amazon
Route 53 can be used to target traffic to ELB, which distributes the traffic to the target compute
instances. You can also use Amazon API Gateway along with AWS Lambda for a serverless solution.
Customers can also run workloads in multiple AWS Regions. With multi-site active/active pattern,
the workload can serve traffic from multiple Regions. With a multi-site active/passive pattern, the
workload serves traffic from the active region while data is replicated to the secondary region and
becomes active in the event of a failure in the primary region. Route 53 health checks can then be
used to control DNS failover from any endpoint in a primary Region to an endpoint in a secondary
Region, verifying that your workload is reachable and available to your users.
Amazon CloudFront provides a simple API for distributing content with low latency and high data
transfer rates by serving requests using a network of edge locations around the world. Content
delivery networks (CDNs) serve customers by serving content located or cached at a location near
to the user. This also improves availability of your application as the load for content is shifted
away from your servers over to CloudFront’s edge locations. The edge locations and regional edge
caches hold cached copies of your content close to your viewers resulting in quick retrieval and
increasing reachability and availability of your workload.
For workloads with users spread out geographically, AWS Global Accelerator helps you improve
the availability and performance of the applications. AWS Global Accelerator provides Anycast
static IP addresses that serve as a fixed entry point to your application hosted in one or more
AWS Regions. This allows traffic to ingress onto the AWS global network as close to your users as
possible, improving reachability and availability of your workload. AWS Global Accelerator also
monitors the health of your application endpoints by using TCP, HTTP, and HTTPS health checks.
Any changes in the health or configuration of your endpoints permit redirection of user traffic to
healthy endpoints that deliver the best performance and availability to your users. In addition, AWS
