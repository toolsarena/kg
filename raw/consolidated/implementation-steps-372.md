---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 594
---

# Implementation steps

1. Write unit tests before you write functional code (test-driven development, or TDD). Establish
code guidelines so that writing and running unit tests are a non-functional coding requirement.
2. Create a suite of automated integration tests that cover the identified testable functionalities.
These tests should simulate user interactions and validate the expected outcomes.
3. Create the necessary test environment to run the integration tests. This may include staging or
pre-production environments that closely mimic the production environment.
