---
title: "There are two main strategies for this deployment:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 599
---

# There are two main strategies for this deployment:

Canary deployment: The practice of directing a small number of your customers to the new
version, usually running on a single service instance (the canary). You then deeply scrutinize any
behavior changes or errors that are generated. You can remove traffic from the canary if you
encounter critical problems and send the users back to the previous version. If the deployment
is successful, you can continue to deploy at your desired velocity, while monitoring the changes
for errors, until you are fully deployed. AWS CodeDeploy can be configured with a deployment
configuration that allows a canary deployment.
Blue/green deployment: Similar to the canary deployment, except that a full fleet of the
application is deployed in parallel. You alternate your deployments across the two stacks (blue
and green). Once again, you can send traffic to the new version, and fall back to the old version
if you see problems with the deployment. Commonly all traffic is switched at once, however you
can also use fractions of your traffic to each version to dial up the adoption of the new version
using the weighted DNS routing capabilities of Amazon Route 53. AWS CodeDeploy and AWS
Elastic Beanstalk can be configured with a deployment configuration that allows a blue/green
deployment.
