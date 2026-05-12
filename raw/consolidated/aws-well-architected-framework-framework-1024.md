---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 361
---

# AWS Well-Architected Framework Framework

your cloud environment. Security Hub seamlessly integrates with Amazon GuardDuty, Amazon
Inspector, Amazon Macie, and AWS Security Hub CSPM. Correlated findings in Security Hub can
result in a net-new finding, called an exposure finding, which includes an assumed attack path
based on vulnerabilities found in each resource.
While some non-compliant resource situations are unique and require human judgment to
remediate, other situations have a standard response that you can define programmatically. For
example, a standard response to a misconfigured VPC security group could be to remove the
disallowed rules and notify the owner. Responses can be defined in AWS Lambda functions, AWS
Systems Manager Automation documents, or through other code environments you prefer. Make
sure the environment is able to authenticate to AWS using an IAM role with the least amount of
permission needed to take corrective action.
Once you define the desired remediation, you can then determine your preferred means
for initiating it. AWS Config can initiate remediations for you. If you are using Security Hub
CSPM, you can do this through custom actions, which publishes the finding information to
Amazon EventBridge. An EventBridge rule can then initiate your remediation. You can configure
remediations through Security Hub CSPM to run either automatically or manually.
For programmatic remediation, we recommend that you have comprehensive logs and audits
for the actions taken, as well as their outcomes. Review and analyze these logs to assess the
effectiveness of the automated processes, and identify areas of improvement. Capture logs in
Amazon CloudWatch Logs and remediation outcomes as finding notes in Security Hub CSPM.
As a starting point, consider Automated Security Response on AWS, which has pre-built
remediations for resolving common security misconfigurations.
