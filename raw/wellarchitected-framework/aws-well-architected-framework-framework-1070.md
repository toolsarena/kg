---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 419
---

# AWS Well-Architected Framework Framework

While it is common practice to encrypt north-south traffic, securing east-west traffic using
authenticated protocols is less common. Modern security practices recommend that network
design alone does not grant a trusted relationship between two entities. When two services may
reside within a common network boundary, it is still best practice to encrypt, authenticate, and
authorize communications between those services.
As an example, AWS service APIs use the AWS Signature Version 4 (SigV4) signature protocol to
authenticate the caller, no matter what network the request originates from. This authentication
ensures that AWS APIs can verify the identity that requested the action, and that identity can then
be combined with policies to make an authorization decision to determine whether the action
should be allowed or not.
Services such as Amazon VPC Lattice and Amazon API Gateway allow you use the same SigV4
signature protocol to add authentication and authorization to east-west traffic in your own
workloads. If resources outside of your AWS environment need to communicate with services
that require SigV4-based authentication and authorization, you can use AWS Identity and
Access Management (IAM) Roles Anywhere on the non-AWS resource to acquire temporary AWS
credentials. These credentials can be used to sign requests to services using SigV4 to authorize
access.
Another common mechanism for authenticating east-west traffic is TLS mutual authentication
(mTLS). Many Internet of Things (IoT), business-to-business applications, and microservices use
mTLS to validate the identity of both sides of a TLS communication through the use of both client
and server-side X.509 certificates. These certificates can be issued by AWS Private Certificate
Authority (AWS Private CA). You can use services such as Amazon API Gateway to provide mTLS
authentication for inter- or intra-workload communication. Application Load Balancer also
supports mTLS for internal or external facing workloads. While mTLS provides authentication
information for both sides of a TLS communication, it does not provide a mechanism for
authorization.
Finally, OAuth 2.0 and OpenID Connect (OIDC) are two protocols typically used for controlling
access to services by users, but are now becoming popular for service-to-service traffic as well.
API Gateway provides a JSON Web Token (JWT) authorizer, allowing workloads to restrict access
to API routes using JWTs issued from OIDC or OAuth 2.0 identity providers. OAuth2 scopes can
be used as a source for basic authorization decisions, but the authorization checks still need to
be implemented in the application layer, and OAuth2 scopes alone cannot support more complex
authorization needs.
