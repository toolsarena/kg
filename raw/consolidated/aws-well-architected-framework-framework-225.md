---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 302
---

# AWS Well-Architected Framework Framework

these credentials, as well as the storage, use, and rotation of API tokens, passwords, and other
credentials.
AWS Secrets Manager provides five key capabilities to ensure the secure storage and handling of
sensitive credentials: encryption at rest, encryption in transit, comprehensive auditing, fine-grained
access control, and extensible credential rotation. Other secret management services from AWS
Partners or locally developed solutions that provide similar capabilities and assurances are also
acceptable.
When you retrieve a secret, you can use the Secrets Manager client side caching components to
cache it for future use. Retrieving a cached secret is faster than retrieving it from Secrets Manager.
Additionally, because there is a cost for calling Secrets Manager APIs, using a cache can reduce your
costs. For all of the ways you can retrieve secrets, see Get secrets.
