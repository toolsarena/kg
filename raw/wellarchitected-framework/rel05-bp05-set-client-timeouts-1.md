---
title: "REL05-BP05 Set client timeouts"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 550
---

# REL05-BP05 Set client timeouts

Set timeouts appropriately on connections and requests, verify them systematically, and do not
rely on default values as they are not aware of workload specifics.
Desired outcome: Client timeouts should consider the cost to the client, server, and workload
associated with waiting for requests that take abnormal amounts of time to complete. Since it is
not possible to know the exact cause of any timeout, clients must use knowledge of services to
develop expectations of probable causes and appropriate timeouts
Client connections time out based on configured values. After encountering a timeout, clients make
decisions to back off and retry or open a circuit breaker. These patterns avoid issuing requests that
may exacerbate an underlying error condition.
