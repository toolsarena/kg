---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 437
---

# AWS Well-Architected Framework Framework

applied to all the incident response roles across all accounts. You might wish to create a separate
IAM policy for each playbook to allow easier management and auditing. Example playbooks
could include response plans for ransomware, data breaches, loss of production access, and other
scenarios.
Use the incident response accounts to assume dedicated incident response IAM roles in other AWS
accounts. These roles must be configured to only be assumable by users in the security account,
and the trust relationship must require that the calling principal has authenticated using MFA. The
roles must use tightly-scoped IAM policies to control access. Ensure that all AssumeRole requests
for these roles are logged in CloudTrail and alerted on, and that any actions taken using these roles
are logged.
It is strongly recommended that both the IAM accounts and the IAM roles are clearly named to
allow them to be easily found in CloudTrail logs. An example of this would be to name the IAM
accounts <USER_ID>-BREAK-GLASS and the IAM roles BREAK-GLASS-ROLE.
CloudTrail is used to log API activity in your AWS accounts and should be used to configure alerts
on usage of the incident response roles. Refer to the blog post on configuring alerts when root
keys are used. The instructions can be modified to configure the Amazon CloudWatch metric filter-
to-filter on AssumeRole events related to the incident response IAM role:
{ $.eventName = "AssumeRole" && $.requestParameters.roleArn =
"<INCIDENT_RESPONSE_ROLE_ARN>" && $.userIdentity.invokedBy NOT EXISTS && $.eventType !
= "AwsServiceEvent" }
As the incident response roles are likely to have a high level of access, it is important that these
alerts go to a wide group and are acted upon promptly.
During an incident, it is possible that a responder might require access to systems which are not
directly secured by IAM. These could include Amazon Elastic Compute Cloud instances, Amazon
Relational Database Service databases, or software-as-a-service (SaaS) platforms. It is strongly
recommended that rather than using native protocols such as SSH or RDP, AWS Systems Manager
Session Manager is used for all administrative access to Amazon EC2 instances. This access can be
controlled using IAM, which is secure and audited. It might also be possible to automate parts of
your playbooks using AWS Systems Manager Run Command documents, which can reduce user
error and improve time to recovery. For access to databases and third-party tools, we recommend
storing access credentials in AWS Secrets Manager and granting access to the incident responder
roles.
