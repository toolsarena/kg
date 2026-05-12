---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 283
---

# AWS Well-Architected Framework Framework

Environment Using Multiple Accounts to configure these services in their own accounts that are
separate from other deployment pipelines.
You can also define templates to standardize defining and deploying AWS accounts, services,
and configurations. This technique allows a central security team to manage these definitions
and provide them to workload teams through a self-service approach. One way to achieve this
is by using Service Catalog, where you can publish templates as products that workload teams
can incorporate into their own pipeline deployments. If you are using AWS Control Tower, some
templates and controls are available as a starting point. Control Tower also provides the Account
Factory capability, allowing workload teams to create new AWS accounts using the standards
you define. This capability helps remove dependencies on a central team to approve and create
new accounts when they are identified as needed by your workload teams. You may need these
accounts to isolate different workload components based on reasons such as the function they
serve, the sensitivity of data being processed, or their behavior.
