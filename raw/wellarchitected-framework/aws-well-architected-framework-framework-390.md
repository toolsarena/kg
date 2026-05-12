---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 514
---

# AWS Well-Architected Framework Framework

• Service contracts and business logic don’t express entities in a common and consistent domain
language, resulting in translation layers that complicate systems and increase debugging efforts.
Benefits of establishing this best practice: Applications are designed as independent services
bounded by business domains and use a common business language. Services are independently
testable and deployable. Services meet domain specific resiliency requirements for the domain
implemented.
Level of risk exposed if this best practice is not established: High
