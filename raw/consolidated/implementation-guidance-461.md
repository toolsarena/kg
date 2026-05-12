---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 603
---

# Implementation guidance

Automate your deployment pipeline. Deployment pipelines allow you to invoke automated testing
and detection of anomalies, and either halt the pipeline at a certain step before production
deployment, or automatically roll back a change. An integral part of this is the adoption of the
culture of continuous integration and continuous delivery/deployment (CI/CD), where a commit
or code change passes through various automated stage gates from build and test stages to
deployment on production environments.
Although conventional wisdom suggests that you keep people in the loop for the most difficult
operational procedures, we suggest that you automate the most difficult procedures for that very
reason.


# Implementation guidance

All AWS data stores offer backup capabilities. Services such as Amazon RDS and Amazon

# Implementation guidance

Control and detect access to backups using authentication and authorization, such as AWS Identity
and Access Management (IAM). Prevent and detect if data integrity of backups is compromised
using encryption.