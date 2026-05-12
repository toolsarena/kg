---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 583
---

# Implementation steps

1. Create and use a source code repository to store the code that controls your infrastructure
configuration. Commit changes to this repository to reflect any ongoing changes you want to
make.
2. Select an infrastructure as code solution such as AWS CloudFormation to keep your
infrastructure up to date and detect inconsistency (drift) from your intended state.
3. Integrate your IaC platform with your CI/CD pipeline to automate deployments.
4. Determine and collect the appropriate metrics for automatic scaling of resources.
5. Configure automatic scaling of resources using scale-out and scale-in policies appropriate for
your workload components. Consider using scheduled scaling for predictable usage patterns.
6. Monitor deployments to detect failures and regressions. Implement rollback mechanisms within
your CI/CD platform to revert changes if necessary.
