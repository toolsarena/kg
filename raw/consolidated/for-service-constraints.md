---
title: "For service constraints:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 473
---

# For service constraints:

• Establish monitoring and metrics methods to alert for resources reading close to their resource
constraints. Leverage CloudWatch as appropriate for metrics or log monitoring.
• Establish alert thresholds for each resource that has a constraint that is meaningful to the
application or system.
• Create workflow and infrastructure management procedures to change the resource type if the
constraint is near utilization. This workflow should include load testing as a best practice to
verify that new type is the correct resource type with the new constraints.
• Migrate identified resource to the recommended new resource type, using existing procedures
and processes.
