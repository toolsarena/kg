---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 461
---

# Implementation guidance

To maintain a robust and reliable application infrastructure, implement secure and automated
deployment practices. This practice involves removing persistent human access from production
environments, using CI/CD tools for deployments, and externalizing environment-specific
configuration data. By following this approach, you can enhance security, reduce the risk of human
errors, and streamline the deployment process.
You can build your AWS account structure to remove persistent human access from production
environments. This practice minimizes the risk of unauthorized changes or accidental
modifications, which improves the integrity of your production systems. Instead of direct
human access, you can use CI/CD tools like AWS CodeBuild and AWS CodePipeline to perform
