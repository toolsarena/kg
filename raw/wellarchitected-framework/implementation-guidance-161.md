---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 594
---

# Implementation guidance

Adopt a test-driven development (TDD) approach to writing software, where you develop test
cases to specify and validate your code. To start, create test cases for each function. If the test
fails, you write new code to pass the test. This approach helps you validate the expected result of
each function. Run unit tests and validate that they pass before you commit code to a source code
repository.
Implement both unit and integration tests as part of the build, test, and deployment stages of the
CI/CD pipeline. Automate testing, and automatically initiate tests whenever a new version of the
application is ready to be deployed. If success criteria are not met, the pipeline is halted or rolled
back.
If the application is a web or mobile app, perform automated integration testing on multiple
desktop browsers or real devices. This approach is particularly useful to validate the compatibility
and functionality of mobile apps across a diverse range of devices.
