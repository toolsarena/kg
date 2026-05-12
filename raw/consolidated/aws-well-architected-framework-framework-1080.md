---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 436
---

# AWS Well-Architected Framework Framework

or role with appropriate permissions to perform tasks and access AWS resources. Use the root
user only for tasks that require root user credentials. To verify that incident responders have the
correct level of access to AWS and other relevant systems, we recommend the pre-provisioning
of dedicated accounts. The accounts require privileged access, and must be tightly controlled
and monitored. The accounts must be built with the fewest privileges required to perform the
necessary tasks, and the level of access should be based on the playbooks created as part of the
incident management plan.
Use purpose-built and dedicated users and roles as a best practice. Temporarily escalating user or
role access through the addition of IAM policies both makes it unclear what access users had during
the incident, and risks the escalated privileges not being revoked.
It is important to remove as many dependencies as possible to verify that access can be gained
under the widest possible number of failure scenarios. To support this, create a playbook to verify
that incident response users are created as users in a dedicated security account, and not managed
through any existing Federation or single sign-on (SSO) solution. Each individual responder must
have their own named account. The account configuration must enforce strong password policy
and multi-factor authentication (MFA). If the incident response playbooks only require access to
the AWS Management Console, the user should not have access keys configured and should be
explicitly disallowed from creating access keys. This can be configured with IAM policies or service
control policies (SCPs) as mentioned in the AWS Security Best Practices for AWS Organizations
SCPs. The users should have no privileges other than the ability to assume incident response roles
in other accounts.
During an incident it might be necessary to grant access to other internal or external individuals to
support investigation, remediation, or recovery activities. In this case, use the playbook mechanism
mentioned previously, and there must be a process to verify that any additional access is revoked
immediately after the incident is complete.
To verify that the use of incident response roles can be properly monitored and audited, it is
essential that the IAM accounts created for this purpose are not shared between individuals, and
that the AWS account root user is not used unless required for a specific task. If the root user is
required (for example, IAM access to a specific account is unavailable), use a separate process with a
playbook available to verify availability of the root user sign-in credentials and MFA token.
To configure the IAM policies for the incident response roles, consider using IAM Access Analyzer
to generate policies based on AWS CloudTrail logs. To do this, grant administrator access to
the incident response role on a non-production account and run through your playbooks. Once
complete, a policy can be created that allows only the actions taken. This policy can then be
