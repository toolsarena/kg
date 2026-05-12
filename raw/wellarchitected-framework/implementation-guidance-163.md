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
