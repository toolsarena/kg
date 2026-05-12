---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 268
---

# Implementation steps

1. Design an organizational unit structure: A properly designed organizational unit structure
reduces the management burden required to create and maintain service control policies and
other security controls. Your organizational unit structure should be aligned with your business
needs, data sensitivity, and workload structure.
2. Create a landing zone for your multi-account environment: A landing zone provides a
consistent security and infrastructure foundation from which your organization can quickly
develop, launch, and deploy workloads. You can use a custom-built landing zone or AWS Control
Tower to orchestrate your environment.
3. Establish guardrails: Implement consistent security guardrails for your environment through
your landing zone. AWS Control Tower provides a list of mandatory and optional controls that
can be deployed. Mandatory controls are automatically deployed when implementing Control
