---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 515
---

# AWS Well-Architected Framework Framework

• Decomposing monoliths into microservices outlines patterns for refactoring microservices. Using
patterns for decomposition by business capability, subdomain, or transaction aligns well with
domain-driven approaches.
• Tactical techniques such as the bubble context allow you to introduce DDD in existing or legacy
applications without up-front rewrites and full commitments to DDD. In a bubble context
approach, a small bounded context is established using a service mapping and coordination, or
anti-corruption layer, which protects the newly defined domain model from external influences.
After teams have performed domain analysis and defined entities and service contracts, they can
take advantage of AWS services to implement their domain-driven design as cloud-based services.
• Start your development by defining tests that exercise business rules of your domain. Test-driven
development (TDD) and behavior-driven development (BDD) help teams keep services focused
on solving business problems.
• Select the AWS services that best meet your business domain requirements and microservice
architecture:
• AWS Serverless allows your team focus on specific domain logic instead of managing servers
and infrastructure.
• Containers at AWS simplify the management of your infrastructure, so you can focus on your
domain requirements.
• Purpose built databases help you match your domain requirements to the best fit database
type.
• Building hexagonal architectures on AWS outlines a framework to build business logic into
services working backwards from a business domain to fulfill functional requirements and then
attach integration adapters. Patterns that separate interface details from business logic with
AWS services help teams focus on domain functionality and improve software quality.
