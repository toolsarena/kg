---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 517
---

# Common anti-patterns:

• Creating service APIs without strongly typed schemas. This results in APIs that cannot be used to
generate API bindings and payloads that can’t be programmatically validated.
• Not adopting a versioning strategy, which forces API consumers to update and release or fail
when service contracts evolve.
• Error messages that leak details of the underlying service implementation rather than describe
integration failures in the domain context and language.
• Not using API contracts to develop test cases and mock API implementations to allow for
independent testing of service components.
Benefits of establishing this best practice: Distributed systems composed of components that
communicate over API service contracts can improve reliability. Developers can catch potential
issues early in the development process with type checking during compilation to verify that
requests and responses follow the API contract and required fields are present. API contracts
provide a clear self-documenting interface for APIs and provider better interoperability between
different systems and programming languages.
Level of risk exposed if this best practice is not established: Medium
