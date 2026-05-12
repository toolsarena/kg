---
title: "REL03-BP03 Provide service contracts per API"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 516
---

# REL03-BP03 Provide service contracts per API

Service contracts are documented agreements between API producers and consumers defined in
a machine-readable API definition. A contract versioning strategy allows consumers to continue
using the existing API and migrate their applications to a newer API when they are ready. Producer
deployment can happen any time as long as the contract is followed. Service teams can use the
technology stack of their choice to satisfy the API contract.
Desired outcome: Applications built with service-oriented or microservice architectures are able to
operate independently while having integrated runtime dependency. Changes deployed to an API
