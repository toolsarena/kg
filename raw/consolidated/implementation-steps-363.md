---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 557
---

# Implementation steps

• Identify business-critical components in your workload.
• Each technical component in your workload should be mapped to its relevant business
function and ranked as critical or non-critical. For examples of critical and non-critical
functionality at Amazon, see Any Day Can Be Prime Day: How Amazon.com Search Uses Chaos
Engineering to Handle Over 84K Requests Per Second.
• This is both a technical and business decision, and varies by organization and workload.
• Design and architect the critical components in your workload to withstand failure of non-critical
components.
• During dependency analysis, consider all potential failure modes, and verify that your
emergency lever mechanisms deliver the critical functionality to downstream components.
• Conduct testing to validate the behavior of your critical components during activation of your
emergency levers.
• Avoid bimodal behavior. For more detail, see REL11-BP05 Use static stability to prevent
bimodal behavior.
• Define, monitor, and alert on relevant metrics to initiate the emergency lever procedure.
