---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 117
---

# AWS Well-Architected Framework Framework

• Your customers complain about service unavailability, which primarily stems from failed
deployments. Your SRE team is responsible for the deployment tool, and an automated rollback
for deployments is in their long-term roadmap. In a recent application rollout, one of the
engineers devised a solution to automate rolling back their application to a previous version.
Though their solution can become the pattern for SRE teams, other teams do not adopt, as there
is no process to track such improvements. The organization continues to be plagued with failed
deployments impacting customers and causing further negative sentiment.
• In order to stay compliant, your infosec team oversees a long-established process to rotate
shared SSH keys regularly on behalf of operators connecting to their Amazon EC2 Linux
instances. It takes several days for the infosec teams to complete rotating keys, and you are
blocked from connecting to those instances. No one inside or outside of infosec suggests using
other options on AWS to achieve the same result.
Benefits of establishing this best practice: By decentralizing authority to make decisions and
empowering your teams to decide key decisions, you are able to address issues more quickly with
increasing success rates. In addition, teams start to realize a sense of ownership, and failures are
acceptable. Experimentation becomes a cultural mainstay. Managers and directors do not feel as
though they are micro-managed through every aspect of their work.
Level of risk exposed if this best practice is not established: Medium


# AWS Well-Architected Framework Framework

• One Observability Workshop
• AWS Solutions Library: Application Monitoring with Amazon CloudWatch