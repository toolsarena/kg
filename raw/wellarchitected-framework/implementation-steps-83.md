---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 420
---

# Implementation steps

• Define and document your workload network flows: The first step in implementing a defense-
in-depth strategy is defining your workload’s traffic flows.
• Create a data flow diagram that clearly defines how data is transmitted between different
services that comprise your workload. This diagram is the first step to enforcing those flows
through authenticated network channels.
• Instrument your workload in development and testing phases to validate that the data flow
diagram accurately reflects the workload’s behavior at runtime.
• A data flow diagram can also be useful when performing a threat modeling exercise, as
described in SEC01-BP07 Identify threats and prioritize mitigations using a threat model.
• Establish network controls: Consider AWS capabilities to establish network controls aligned to
your data flows. While network boundaries should not be the only security control, they provide
a layer in the defense-in-depth strategy to protect your workload.
• Use security groups to establish define and restrict data flows between resources.
• Consider using AWS PrivateLink to communicate with both AWS and third-party services that
support AWS PrivateLink. Data sent through a AWS PrivateLink interface endpoint stays within
the AWS network backbone and does not traverse the public Internet.
• Implement authentication and authorization across services in your workload: Choose the
set of AWS services most appropriate to provide authenticated, encrypted traffic flows in your
workload.
• Consider Amazon VPC Lattice to secure service-to-service communication. VPC Lattice can use
SigV4 authentication combined with auth policies to control service-to-service access.
• For service-to-service communication using mTLS, consider API Gateway, Application Load
Balancer. AWS Private CA can be used to establish a private CA hierarchy capable of issuing
certificates for use with mTLS.
• When integrating with services using OAuth 2.0 or OIDC, consider API Gateway using the JWT
authorizer.
• For communication between your workload and IoT devices, consider AWS IoT Core, which
provides several options for network traffic encryption and authentication.
• Monitor for unauthorized access: Continually monitor for unintended communication channels,
unauthorized principals attempting to access protected resources, and other improper access
patterns.
