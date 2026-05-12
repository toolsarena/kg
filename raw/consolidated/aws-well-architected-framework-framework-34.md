---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 50
---

# AWS Well-Architected Framework Framework

key metrics are capturing time-to-first-byte or rendering. Other generally applicable metrics
include thread count, garbage collection rate, and wait states. Business metrics, such as the
aggregate cumulative cost per request, can alert you to ways to drive down costs. Carefully
consider how you plan to interpret metrics. For example, you could choose the maximum or 99th
percentile instead of the average.
• Performance test automatically: As part of your deployment process, automatically start
performance tests after the quicker running tests have passed successfully. The automation
should create a new environment, set up initial conditions such as test data, and then run a series
of benchmarks and load tests. Results from these tests should be tied back to the build so you
can track performance changes over time. For long-running tests, you can make this part of the
pipeline asynchronous from the rest of the build. Alternatively, you could run performance tests
overnight using Amazon EC2 Spot Instances.
• Load generation: You should create a series of test scripts that replicate synthetic or prerecorded
user journeys. These scripts should be idempotent and not coupled, and you might need to
include pre-warming scripts to yield valid results. As much as possible, your test scripts should
replicate the behavior of usage in production. You can use software or software-as-a-service
(SaaS) solutions to generate the load. Consider using AWS Marketplace solutions and Spot
Instances — they can be cost-effective ways to generate the load.
• Performance visibility: Key metrics should be visible to your team, especially metrics against
each build version. This allows you to see any significant positive or negative trend over time.
You should also display metrics on the number of errors or exceptions to make sure you are
testing a working system.
• Visualization: Use visualization techniques that make it clear where performance issues, hot
spots, wait states, or low utilization is occurring. Overlay performance metrics over architecture
diagrams — call graphs or code can help identify issues quickly.
• Regular review process: Architectures performing poorly is usually the result of a non-existent
or broken performance review process. If your architecture is performing poorly, implementing a
performance review process allows you to drive iterative improvement.
• Continual optimization: Adopt a culture to continually optimize the performance efficiency of
your cloud workload.
The following question focuses on these considerations for performance efficiency.


# AWS Well-Architected Framework Framework

• Only penetration testing for package security issues, and not evaluating implemented business
logic.