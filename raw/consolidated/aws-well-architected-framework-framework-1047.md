---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 390
---

# AWS Well-Architected Framework Framework

and the controls in place to protect that data. Additionally, consider using resource tags where
available. For example, you can apply a tag that has a tag key of Classification and a
tag value of PHI for protected health information (PHI), and another tag that has a tag key of
Sensitivity and a tag value of High. Services such as AWS Config can then be used to monitor
these resources for changes and alert if they are modified in a way that brings them out of
compliance with your protection requirements (such as changing the encryption settings). You can
capture the standard definition of your tag keys and acceptable values using tag policies, a feature
of AWS Organizations. It is not recommended that the tag key or value contains private or sensitive
data.


# AWS Well-Architected Framework Framework

• AWS Tag Editor

# AWS Well-Architected Framework Framework

• PERF03-BP01 Use a purpose-built data store that best supports your data access and storage
requirements
• COST04-BP05 Enforce data retention policies