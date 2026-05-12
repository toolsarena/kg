---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 701
---

# Implementation steps

1. Validate that the DR region contains the AWS services and features required for a successful
execution of your DR plan.
2. Use infrastructure as code (IaC). Keep your production infrastructure and application
configuration templates accurate, and regularly apply them to your disaster recovery
environment. AWS CloudFormation can detect drift between what your CloudFormation
templates specify and what is actually deployed.
3. Configure CI/CD pipelines to deploy applications and infrastructure updates to all environments,
including primary and DR sites. CI/CD solutions such as AWS CodePipeline can automate the
deployment process, which reduces the risk of configuration drift.
4. Stagger deployments between the primary and DR environments. This approach allows updates
to be initially deployed and tested in the primary environment, which isolates issues in the
primary site before they are propagated to the DR site. This approach prevents defects from
being simultaneously pushed to production and the DR site at the same time and maintains the
integrity of the DR environment.
5. Continually monitor resource configurations in both primary and DR environments. Solutions
such as AWS Config can help to enforce configuration compliance and detect drift, which helps
maintain the consistent configurations across environments.
6. Implement alerting mechanisms to track and notify upon any configuration drift or data
replication interruption or lag.
7. Automate the remediation of detected configuration drift.
8. Schedule regular audits and compliance checks to verify ongoing alignment between primary
and DR configurations. Periodic reviews help you maintain compliance with defined rules and
identify any discrepancies that need to be addressed.
9. Check for mismatches in AWS provisioned capacity, service quotas, throttle limits, and
configuration and version discrepancies.
