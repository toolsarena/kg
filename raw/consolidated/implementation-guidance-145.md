---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 548
---

# Implementation guidance

Fail fast strategies can be coded into software solutions as well as configured into infrastructure.
In addition to failing fast, queues are a straightforward yet powerful architectural technique to
decouple system components smooth load. Amazon CloudWatch provides capabilities to monitor
for and alarm on failures. Once a system is known to be failing, mitigation strategies can be
invoked, including failing away from impaired resources. When systems implement queues with
Amazon SQS and other queue technologies to smooth load, they must consider how to manage
queue backlogs, as well as message consumption failures.
