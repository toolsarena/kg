---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 152
---

# Implementation steps

1. Work with stakeholders in your organization to develop a testing standard for software artifacts.
What standard tests should all artifacts pass? Are there compliance or governance requirements
that must be included in the test coverage? Do you need to conduct code quality tests? When
tests complete, who needs to know?
1. The AWS Deployment Pipeline Reference Architecture contains an authoritative list of types
of tests that can be conducted on software artifacts as part of an integration pipeline.
2. Instrument your application with the necessary tests based on your software testing standard.
Each set of tests should complete in under ten minutes. Tests should run as part of an
integration pipeline.
a. Use Amazon Q Developer, a generative AI tool that can help create unit test cases (including
boundary conditions), generate functions using code and comments, and implement well-
known algorithms.
b. Use Amazon CodeGuru Reviewer to test your application code for defects.
c. You can use AWS CodeBuild to conduct tests on software artifacts.
d. AWS CodePipeline can orchestrate your software tests into a pipeline.
