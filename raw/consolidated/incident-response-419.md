---
title: "Incident response 419"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 424
---

# Incident response 419

|  |  |  |
| --- | --- | --- |
|  | | Role | Name | Contact Information | Responsibilities |
1 | ——– | ——- | ——- | ——- |
2 | Incident Manager | Jane Doe| jane.doe@example.com | Overall authority during
response |
3 | Incident Responder | John Smith | john.smith@example.com | Investigation and
remediation |
4 | Communications Lead | Emily Johnson | emily.johnson@example.com | Internal and
external communications |
5 | Communications Lead | Michael Brown | michael.brown@example.com | Insights on
critical workloads | |  |
|  |  |  |


# Incident response 432

|  |  |  |
| --- | --- | --- |
|  | { $.eventName = "AssumeRole" && $.requestParameters.roleArn =
"<INCIDENT_RESPONSE_ROLE_ARN>" && $.userIdentity.invokedBy NOT EXISTS && $.eventType !
= "AwsServiceEvent" } |  |
|  |  |  |

# Incident response 432

|  |  |  |
| --- | --- | --- |
|  | { $.eventName = "AssumeRole" && $.requestParameters.roleArn =
"<INCIDENT_RESPONSE_ROLE_ARN>" && $.userIdentity.invokedBy NOT EXISTS && $.eventType !
= "AwsServiceEvent" } |  |
|  |  |  |