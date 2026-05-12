---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 184
---

# AWS Well-Architected Framework Framework

b. Consider a continuous testing strategy where appropriate throughout the development
lifecycle.
2. Select automated tools for testing and rollback based on your business requirements and
pipeline investments.
3. Decide which test cases you wish to automate and which should be performed manually. These
can be defined based on business value priority of the feature being tested. Align all team
members to this plan and verify accountability for performing manual tests.
a. Apply automated testing capabilities to specific test cases that make sense for automation,
such as repeatable or frequently run cases, those that require repetitive tasks, or those that
are required across multiple configurations.
b. Define test automation scripts as well as the success criteria in the automation tool so
continued workflow automation can be initiated when specific cases fail.
c. Define specific failure criteria for automated rollback.
4. Prioritize test automation to drive consistent results with thorough test case development where
complexity and human interaction have a higher risk of failure.
5. Integrate your automated testing and rollback tools into your CI/CD pipeline.
a. Develop clear success criteria for your changes.
b. Monitor and observe to detect these criteria and automatically reverse changes when specific
rollback criteria are met.
