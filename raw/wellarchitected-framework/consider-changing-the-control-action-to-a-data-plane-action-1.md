---
title: "Consider changing the control action to a data plane action:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 645
---

# Consider changing the control action to a data plane action:

• Auto Scaling (control plane) to pre-scaled Amazon EC2 resources (data plane)
• Amazon EC2 instance scaling (control plane) to AWS Lambda scaling (data plane)
• Assess any designs using Kubernetes and the nature of the control plane actions. Adding pods
is a data plane action in Kubernetes. Actions should be limited to adding pods and not adding
nodes. Using over-provisioned nodes is the preferred method to limit control plane actions
Consider alternate approaches that allow for data plane actions to affect the same remediation.
• Route 53 Record change (control plane) or Amazon Application Recovery Controller (data plane)
