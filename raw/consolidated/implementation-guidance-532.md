---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 849
---

# Implementation guidance

By effectively tracking the project lifecycle, organizations can achieve better cost control through
enhanced planning, management, and resource optimization. The insights gained through tracking
are invaluable for making informed decisions that contribute to the cost-effectiveness and overall
success of the project.
Tracking the entire lifecycle of the workload helps you understand when workloads or workload
components are no longer required. The existing workloads and components may appear to be
in use, but when AWS releases new services or features, they can be decommissioned or adopted.
Check the previous stages of workloads. After a workload is in production, previous environments
can be decommissioned or greatly reduced in capacity until they are required again.
You can tag resources with a timeframe or reminder to pin the time that the workload was
reviewed. For example, if the development environment was last reviewed months ago, it could be
a good time to review it again to explore if new services can be adopted or if the environment is
in use. You can group and tag your applications with myApplications on AWS to manage and track
metadata such as criticality, environment, last reviewed, and cost center. You can both track your
workload's lifecycle and monitor and manage the cost, health, security posture, and performance
of your applications.
AWS provides various management and governance services you can use for entity lifecycle
tracking. You can use AWS Config or AWS Systems Manager to provide a detailed inventory of
your AWS resources and configuration. It is recommended that you integrate with your existing
project or asset management systems to keep track of active projects and products within your
organization. Combining your current system with the rich set of events and metrics provided by
AWS allows you to build a view of significant lifecycle events and proactively manage resources to
reduce unnecessary costs.
Similar to Application Lifecycle Management (ALM), tracking project lifecycle should involve
multiple processes, tools, and teams working together, such as design and development, testing,
production, support, and workload redundancy.
By carefully monitoring each phase of a project's lifecycle, organizations gain crucial insights and
enhanced control, facilitating successful project planning, implementation, and completion. This
careful oversight verifies that projects not only meet quality standards, but are delivered on time
and within budget, promoting overall cost efficiency.
