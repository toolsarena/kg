---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 470
---

# Common anti-patterns:

• Deploying a workload without understanding the hard or soft quotas and their limits for the
services used.
• Deploying a replacement workload without analyzing and reconfiguring the necessary quotas or
contacting Support in advance.
• Assuming that cloud services have no limits and the services can be used without consideration
to rates, limits, counts, quantities.
• Assuming that quotas will automatically be increased.
• Not knowing the process and timeline of quota requests.
• Assuming that the default cloud service quota is the identical for every service compared across
regions.
• Assuming that service constraints can be breached and the systems will auto-scale or add
increase the limit beyond the resource’s constraints
• Not testing the application at peak traffic in order to stress the utilization of its resources.
• Provisioning the resource without analysis of the required resource size.
• Overprovisioning capacity by choosing resource types that go well beyond actual need or
expected peaks.
• Not assessing capacity requirements for new levels of traffic in advance of a new customer event
or deploying a new technology.
Benefits of establishing this best practice: Monitoring and automated management of service
quotas and resource constraints can proactively reduce failures. Changes in traffic patterns for
a customer’s service can cause a disruption or degradation if best practices are not followed. By


# Common anti-patterns:

• Allowing resource usage in one isolation Region to grow with no mechanism to maintain capacity
in the other ones.
• Manually setting all quotas independently in isolation Regions.