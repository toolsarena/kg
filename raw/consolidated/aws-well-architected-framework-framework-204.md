---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 276
---

# AWS Well-Architected Framework Framework

configurations and actions across your AWS Organizations using service control policies (SCP).
Implement rules in AWS Config to monitor and report on non-compliant resources, then switch
rules to an enforcement model once confident in their behavior. To deploy sets of pre-defined and
managed rules that align to your cybersecurity frameworks, evaluate the use of AWS Security Hub
CSPM standards as your first option. The AWS Foundational Service Best Practices (FSBP) standard
and the CIS AWS Foundations Benchmark are good starting points with controls that align to many
objectives that are shared across multiple standard frameworks. Where Security Hub CSPM does
not intrinsically have the control detections desired, it can be complemented using AWS Config
conformance packs.
Use APN Partner Bundles recommended by the AWS Global Security and Compliance Acceleration
(GSCA) team to get assistance from security advisors, consulting agencies, evidence collection and
reporting systems, auditors, and other complementary services when required.


# AWS Well-Architected Framework Framework

• COST02-BP01 Develop policies based on your organization requirements