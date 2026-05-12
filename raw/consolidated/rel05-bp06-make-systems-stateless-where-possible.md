---
title: "REL05-BP06 Make systems stateless where possible"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 554
---

# REL05-BP06 Make systems stateless where possible

Systems should either not require state, or should offload state such that between different client
requests, there is no dependence on locally stored data on disk and in memory. This allows servers
to be replaced at will without causing an availability impact.
When users or services interact with an application, they often perform a series of interactions that
form a session. A session is unique data for users that persists between requests while they use
the application. A stateless application is an application that does not need knowledge of previous
interactions and does not store session information.
Once designed to be stateless, you can then use serverless compute services, such as AWS Lambda
or AWS Fargate.
