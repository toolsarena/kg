---
title: "REL05-BP04 Fail fast and limit queues"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 547
---

# REL05-BP04 Fail fast and limit queues

When a service is unable to respond successfully to a request, fail fast. This allows resources
associated with a request to be released, and permits a service to recover if it’s running out of
resources. Failing fast is a well-established software design pattern that can be leveraged to build
highly reliable workloads in the cloud. Queuing is also a well-established enterprise integration
pattern that can smooth load and allow clients to release resources when asynchronous processing
can be tolerated. When a service is able to respond successfully under normal conditions but fails
when the rate of requests is too high, use a queue to buffer requests. However, do not allow a
buildup of long queue backlogs that can result in processing stale requests that a client has already
given up on.
Desired outcome: When systems experience resource contention, timeouts, exceptions, or grey
failures that make service level objectives unachievable, fail fast strategies allow for faster system
recovery. Systems that must absorb traffic spikes and can accommodate asynchronous processing
can improve reliability by allowing clients to quickly release requests by using queues to buffer
requests to backend services. When buffering requests to queues, queue management strategies
are implemented to avoid insurmountable backlogs.
