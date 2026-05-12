---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 532
---

# AWS Well-Architected Framework Framework

• You use timestamps as keys for idempotency. This can cause inaccuracies due to clock skew or
due to multiple clients that use the same timestamps to apply changes.
• You store entire payloads for idempotency. In this approach, you save complete data payloads
for every request and overwrite it at each new request. This can degrade performance and affect
scalability.
• You generate keys inconsistently across services. Without consistent keys, services may fail to
recognize duplicate requests, which results in unintended results.
