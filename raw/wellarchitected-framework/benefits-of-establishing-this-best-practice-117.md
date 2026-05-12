---
title: "Benefits of establishing this best practice:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 532
---

# Benefits of establishing this best practice:

• Greater scalability: The system can handle retries and duplicate requests without having to
perform additional logic or complex state management.
• Enhanced reliability: Idempotency helps services handle multiple identical requests in a
consistent manner, which reduces the risk of unintended side effects or duplicate records. This is
especially crucial in distributed systems, where network failures and retries are common.
• Improved data consistency: Because the same request produces the same response, idempotency
helps maintain data consistency across distributed systems. This is essential to maintain the
integrity of transactions and operations.
• Error handling: Idempotency tokens make error handling more straightforward. If a client
does not receive a response due to an issue, it can safely resend the request with the same
idempotency token.
• Operational transparency: Idempotency allows for better monitoring and logging. Services can
log requests with their idempotency tokens, which makes it easier to trace and debug issues.
• Simplified API contract: It can simplify the contract between the client and server side systems
and reduce the fear of erroneous data processing.
Level of risk exposed if this best practice is not established: Medium
