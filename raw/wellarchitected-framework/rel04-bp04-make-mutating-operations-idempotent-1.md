---
title: "REL04-BP04 Make mutating operations idempotent"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 531
---

# REL04-BP04 Make mutating operations idempotent

An idempotent service promises that each request is processed exactly once, such that making
multiple identical requests has the same effect as making a single request. This makes it easier for
a client to implement retries without fear that a request is erroneously processed multiple times.
To do this, clients can issue API requests with an idempotency token, which is used whenever the
request is repeated. An idempotent service API uses the token to return a response identical to the
response that was returned the first time that the request was completed, even if the underlying
state of the system has changed.
In a distributed system, it is relatively simple to perform an action at most once (client makes only
one request) or at least once (keep requesting until client gets confirmation of success). It is more
difficult to guarantee an action is performed exactly once, such that making multiple identical
requests has the same effect as making a single request. Using idempotency tokens in APIs,
services can receive a mutating request one or more times without the need to create duplicate
records or side effects.
Desired outcome: You have a consistent, well-documented, and widely adopted approach for
ensuring idempotency across all components and services.
