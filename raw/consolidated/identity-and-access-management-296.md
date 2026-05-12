---
title: "Identity and access management 296"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 301
---

# Identity and access management 296

| Credential type | Description | Suggested strategy |
| --- | --- | --- |
| Application and database
credentials | Passwords – plain text string | Rotate: Store credentials in
AWS Secrets Manager and
establish automated rotation
if possible. |
| Amazon RDS and Aurora
Admin Database credentials | Passwords – plain text string | Replace: Use the Secrets
Manager integration with
Amazon RDS or Amazon
Aurora. In addition, some RDS
database types can use IAM
roles instead of passwords
for some use cases (for more
detail, see IAM database
authentication). |
| OAuth tokens | Secret tokens – plain text
string | Rotate: Store tokens in
AWS Secrets Manager and
configure automated rotation. |
| API tokens and keys | Secret tokens – plain text
string | Rotate: Store in AWS Secrets
Manager and establish
automated rotation if
possible. |


# Identity and access management 297

|  |  |  |
| --- | --- | --- |
|  | Note
Some languages may require you to implement your own in-memory encryption for client
side caching. |  |
|  |  |  |

# Identity and access management 297

|  |  |  |
| --- | --- | --- |
|  | Note
Some languages may require you to implement your own in-memory encryption for client
side caching. |  |
|  |  |  |