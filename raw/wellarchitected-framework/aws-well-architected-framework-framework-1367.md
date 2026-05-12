---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 818
---

# AWS Well-Architected Framework Framework

Budgets alerts based on actual costs, which are reactive in nature, or on forecasted costs, which
provides time to implement mitigations against potential cost overruns. You can be alerted
when your cost or usage actually exceeds a certain level or if they are forecasted to exceed your
budgeted amount.
Adjust existing budget and forecast processes to be more dynamic using trend-based algorithms
(with historical costs as inputs) and driver-based algorithms (for example, new product launches,
Regional expansion, or new environments for workloads), which are ideal for a dynamic and
variable spending environment. Once you've determined your trend-based forecast using Cost
Explorer or any other tools, use the AWS Pricing Calculator to estimate your AWS use case and
future costs based on the expected usage (traffic, requests-per-second, or required Amazon EC2
instances).
Track the accuracy of that forecast, as budgets should be set based on these forecast calculations
and estimations. Monitor the accuracy and effectiveness of the integrated cloud cost forecasts.
Regularly review actual spend compared to your forecast, and adjust as needed to improve forecast
precision. Track forecast variance, and perform root cause analysis on reported variance to act and
adjust forecasts.
As mentioned in the COST01-BP02 Establish a partnership between finance and technology, it
is important to foster a partnership and cadence between IT, finance, and other stakeholders to
verify that they are all using the same tools or processes for consistency. In cases where budgets
may need to change, increase cadence touch points to react to those changes more quickly.
