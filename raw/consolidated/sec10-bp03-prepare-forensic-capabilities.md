---
title: "SEC10-BP03 Prepare forensic capabilities"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 430
---

# SEC10-BP03 Prepare forensic capabilities

Ahead of a security incident, consider developing forensics capabilities to support security event
investigations.
Level of risk exposed if this best practice is not established: Medium
Concepts from traditional on-premises forensics apply to AWS. For key information to start
building forensics capabilities in the AWS Cloud, see Forensic investigation environment strategies
in the AWS Cloud.
Once you have your environment and AWS account structure set up for forensics, define the
technologies required to effectively perform forensically sound methodologies across the four
phases:
• Collection: Collect relevant AWS logs, such as AWS CloudTrail, AWS Config, VPC Flow Logs, and
host-level logs. Collect snapshots, backups, and memory dumps of impacted AWS resources
where available.
• Examination: Examine the data collected by extracting and assessing the relevant information.
• Analysis: Analyze the data collected in order to understand the incident and draw conclusions
from it.
• Reporting: Present the information resulting from the analysis phase.
