---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 367
---

# AWS Well-Architected Framework Framework

further control using additional services, such as AWS PrivateLink, Amazon Route 53 Resolver DNS
Firewall, AWS Network Firewall, and AWS WAF.
Understand and inventory the data flow and communication requirements of your workloads in
terms of connection-initiating parties, ports, protocols, and network layers. Evaluate the protocols
available for establishing connections and transmitting data to select ones that achieve your
protection requirements (for example, HTTPS rather than HTTP). Capture these requirements
at both the boundaries of your networks and within each layer. Once these requirements are
identified, explore options to only allow the required traffic to flow at each connection point. A
good starting point is to use security groups within your VPC, as they can be attached to resources
that uses an Elastic Network Interface (ENI), such Amazon EC2 instances, Amazon ECS tasks,
Amazon EKS pods, or Amazon RDS databases. Unlike a Layer 4 firewall, a security group can have
a rule that allows traffic from another security group by its identifier, minimizing updates as
resources within the group change over time. You can also filter traffic using both inbound and
outbound rules using security groups.
When traffic moves between VPCs, it's common to use VPC peering for simple routing or the
AWS Transit Gateway for complex routing. With these approaches, you facilitate traffic flows
between the range of IP addresses of both the source and destination networks. However, if your
workload only requires traffic flows between specific components in different VPCs, consider
using a point-to-point connection using AWS PrivateLink. To do this, identify which service should
act as the producer and which should act as the consumer. Deploy a compatible load balancer
for the producer, turn on PrivateLink accordingly, and then accept a connection request by the
consumer. The producer service is then assigned a private IP address from the consumer's VPC
that the consumer can use to make subsequent requests. This approach reduces the need to
peer the networks. Include the costs for data processing and load balancing as part of evaluating
PrivateLink.
While security groups and PrivateLink help control the flow between the components of your
workloads, another major consideration is how to control which DNS domains your resources are
allowed to access (if any). Depending on the DHCP configuration of your VPCs, you can consider
two different AWS services for this purpose. Most customers use the default Route 53 Resolver
DNS service (also called Amazon DNS server or AmazonProvidedDNS) available to VPCs at the +2
address of its CIDR range. With this approach, you can create DNS Firewall rules and associate them
to your VPC that determine what actions to take for the domain lists you supply.
If you are not using the Route 53 Resolver, or if you want to complement the Resolver with deeper
inspection and flow control capabilities beyond domain filtering, consider deploying an AWS
