---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 174
---

# Common anti-patterns:

• You performed a deployment and your application has become unstable but there appear to be
active users on the system. You have to decide whether to rollback the change and impact the
active users or wait to rollback the change knowing the users may be impacted regardless.
• After making a routine change, your new environments are accessible, but one of your subnets
has become unreachable. You have to decide whether to rollback everything or try to fix the
inaccessible subnet. While you are making that determination, the subnet remains unreachable.
• Your systems are not architected in a way that allows them to be updated with smaller releases.
As a result, you have difficulty in reversing those bulk changes during a failed deployment.
• You do not use infrastructure as code (IaC) and you made manual updates to your infrastructure
that resulted in an undesired configuration. You are unable to effectively track and revert the
manual changes.
• Because you have not measured increased frequency of your deployments, your team is not
incentivized to reduce the size of their changes and improve their rollback plans for each change,
leading to more risk and increased failure rates.
• You do not measure the total duration of an outage caused by unsuccessful changes. Your team
is unable to prioritize and improve its deployment process and recovery plan effectiveness.
Benefits of establishing this best practice: Having a plan to recover from unsuccessful changes
minimizes the mean time to recover (MTTR) and reduces your business impact.
Level of risk exposed if this best practice is not established: High


# Common anti-patterns:

• You commit code to the main branch of your application without a code review. The change
automatically deploys to production and causes an outage.