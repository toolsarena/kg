---
title: "Service-oriented architectures (SOA) define services with well-delineated functions defined by"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 513
---

# Service-oriented architectures (SOA) define services with well-delineated functions defined by

business needs. Microservices use domain models and bounded context to draw service boundaries
along business context boundaries. Focusing on business domains and functionality helps teams
define independent reliability requirements for their services. Bounded contexts isolate and
encapsulate business logic, allowing teams to better reason about how to handle failures.
Desired outcome: Engineers and business stakeholders jointly define bounded contexts and
use them to design systems as services that fulfill specific business functions. These teams use
established practices like event storming to define requirements. New applications are designed
as services well-defined boundaries and loosely coupling. Existing monoliths are decomposed
into bounded contexts and system designs move towards SOA or microservice architectures.
When monoliths are refactored, established approaches like bubble contexts and monolith
decomposition patterns are applied.
Domain-oriented services are executed as one or more processes that don’t share state. They
independently respond to fluctuations in demand and handle fault scenarios in light of domain
specific requirements.
