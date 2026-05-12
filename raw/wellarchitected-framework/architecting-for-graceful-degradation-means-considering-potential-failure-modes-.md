---
title: "Architecting for graceful degradation means considering potential failure modes during"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 538
---

# Architecting for graceful degradation means considering potential failure modes during

dependency design. For each failure mode, have a way to deliver most or at least the most
critical functionality of the component to callers or customers. These considerations can become
additional requirements that can be tested and verified. Ideally, a component is able to perform its
core function in an acceptable manner even when one or multiple dependencies fail.
This is as much a business discussion as a technical one. All business requirements are important
and should be fulfilled if possible. However, it still makes sense to ask what should happen when
not all of them can be fulfilled. A system can be designed to be available and consistent, but
under circumstances where one requirement must be dropped, which one is more important? For
payment processing, it might be consistency. For a real-time application, it might be availability.
For a customer facing website, the answer may depend on customer expectations.
What this means depends on the requirements of the component and what should be considered
its core function. For example:
• An ecommerce website might display data from multiple different systems like personalized
recommendations, highest ranked products, and status of customer orders on the landing
page. When one upstream system fails, it still makes sense to display everything else instead of
showing an error page to a customer.
• A component performing batch writes can still continue processing a batch if one of the
individual operations fails. It should be simple to implement a retry mechanism. This can be
done by returning information on which operations succeeded, which failed, and why they failed
to the caller, or putting failed requests into a dead letter queue to implement asynchronous
retries. Information about failed operations should be logged as well.
• A system that processes transactions must verify that either all or no individual updates are
executed. For distributed transactions, the saga pattern can be used to roll back previous
