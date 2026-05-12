---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 289
---

# Implementation guidance

AWS informs customers of new security services and features through several channels:
• AWS What's New
• AWS News Blog
• AWS Security Blog
• AWS Security Bulletins
• AWS documentation overview
You can subscribe to an AWS Daily Feature Updates topic using Amazon Simple Notification Service
(Amazon SNS) for a comprehensive daily summary of updates. Some security services, such as
Amazon GuardDuty and AWS Security Hub CSPM, provide their own SNS topics to stay informed
about new standards, findings, and other updates for those particular services.
New services and features are also announced and described in detail during conferences, events,
and webinars conducted around the globe each year. Of particular note is the annual AWS
re:Inforce security conference and the more general AWS re:Invent conference. The previously-
mentioned AWS news channels share these conference announcements about security and other
services, and you can view deep dive educational breakout sessions online at the AWS Events
channel on YouTube.
You can also ask your AWS account team about the latest security service updates and
recommendations. You can reach out to your team through the Sales Support form if you do not
have their direct contact information. Similarly, if you subscribed to AWS Enterprise Support, you
will receive weekly updates from your Technical Account Manager (TAM) and can schedule a regular
review meeting with them.


# Implementation guidance

There are several ways for human identities to sign in to AWS. It is an AWS best practice to rely on
a centralized identity provider using federation (direct SAML 2.0 federation between AWS IAM and