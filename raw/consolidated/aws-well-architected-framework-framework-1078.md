---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 431
---

# AWS Well-Architected Framework Framework

• Log archival: Aggregate logs in a log archival AWS account with limited permissions.
• Security tools: Centralize security services in a security tool AWS account. This account operates
as the delegated administrator for security services.
Within the forensics OU, you have the option to implement a single forensics account or accounts
for each Region that you operate in, depending on which works best for your business and
operational model. If you create a forensics account per Region, you can block the creation of AWS
resources outside of that Region and reduce the risk of resources being copied to an unintended
region. For example, if you only operate in US East (N. Virginia) Region (us-east-1) and US West
(Oregon) (us-west-2), then you would have two accounts in the forensics OU: one for us-east-1
and one for us-west-2.
You can create a forensics AWS account for multiple Regions. You should exercise caution in
copying AWS resources to that account to verify you’re aligning with your data sovereignty
requirements. Because it takes time to provision new accounts, it is imperative to create and
instrument the forensics accounts well ahead of an incident so that responders can be prepared to
effectively use them for response.
The following diagram displays a sample account structure including a forensics OU with per-
