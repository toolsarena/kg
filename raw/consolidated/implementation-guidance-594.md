---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 998
---

# Implementation guidance

Use automation and infrastructure-as-code to bring build environments up when needed and take
them down when not used. A common pattern is to schedule periods of availability that coincide
with the working hours of your development team members. Your test environments should
closely resemble the production configuration. However, look for opportunities to use instance
types with burst capacity, Amazon EC2 Spot Instances, automatic scaling database services,
containers, and serverless technologies to align development and test capacity with use. Limit data
volume to just meet the test requirements. If using production data in test, explore possibilities of
sharing data from production and not moving data across.
