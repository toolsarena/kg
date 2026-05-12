---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 539
---

# AWS Well-Architected Framework Framework

operations in case a later operation of the same transaction fails. Here, the core function is
maintaining consistency.
• Time critical systems should be able to deal with dependencies not responding in a timely
manner. In these cases, the circuit breaker pattern can be used. When responses from a
dependency start timing out, the system can switch to a closed state where no additional call are
made.
• An application may read parameters from a parameter store. It can be useful to create container
images with a default set of parameters and use these in case the parameter store is unavailable.
Note that the pathways taken in case of component failure need to be tested and should be
significantly simpler than the primary pathway. Generally, fallback strategies should be avoided.
