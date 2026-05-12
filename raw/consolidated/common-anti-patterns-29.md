---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 172
---

# Common anti-patterns:

• On Friday, you finish authoring the new code for your feature branch. On Monday, after running
your code quality test scripts and each of your unit tests scripts, you check in your code for the
next scheduled release.
• You are assigned to code a fix for a critical issue impacting a large number of customers in
production. After testing the fix, you commit your code and email change management to
request approval to deploy it to production.
• As a developer, you log into the AWS Management Console to create a new development
environment using non-standard methods and systems.
Benefits of establishing this best practice: By implementing automated build and deployment
management systems, you reduce errors caused by manual processes and reduce the effort to
deploy changes helping your team members to focus on delivering business value. You increase the
speed of delivery as you promote through to production.
Level of risk exposed if this best practice is not established: Low


# Common anti-patterns:

• There is a known performance issue in your application server. It is added to the backlog behind
every planned feature implementation. If the rate of planned features being added remains
constant, the performance issue would never be addressed.

# Common anti-patterns:

• Placing multiple unrelated workloads with different data sensitivity levels into the same account.
• Poorly defined organizational unit (OU) structure.