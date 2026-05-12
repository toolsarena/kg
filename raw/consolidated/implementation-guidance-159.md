---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 590
---

# Implementation guidance

• Perform load testing to identify which aspect of your workload indicates that you must add or
remove capacity. Load testing should have representative traffic similar to what you receive in
production. Increase the load while watching the metrics you have instrumented to determine
which metric indicates when you must add or remove resources.
• Distributed Load Testing on AWS: simulate thousands of connected users
• Identify the mix of requests. You may have varied mixes of requests, so you should look at
various time frames when identifying the mix of traffic.
• Implement a load driver. You can use custom code, open source, or commercial software to
implement a load driver.
• Load test initially using small capacity. You see some immediate effects by driving load onto
a lesser capacity, possibly as small as one instance or container.
• Load test against larger capacity. The effects will be different on a distributed load, so you
must test against as close to a product environment as possible.


# Implementation guidance

Experiments should be run in a safe manner. Leverage multiple environments to experiment
without jeopardizing production resources. Use A/B testing and feature flags to test experiments.
Provide team members the ability to conduct experiments in a sandbox environment.