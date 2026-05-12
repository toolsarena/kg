---
title: "REL05-BP02 Throttle requests"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 540
---

# REL05-BP02 Throttle requests

Throttle requests to mitigate resource exhaustion due to unexpected increases in demand.
Requests below throttling rates are processed while those over the defined limit are rejected with a
return message indicating the request was throttled.
