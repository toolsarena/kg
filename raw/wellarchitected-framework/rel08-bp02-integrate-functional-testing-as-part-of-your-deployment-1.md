---
title: "REL08-BP02 Integrate functional testing as part of your deployment"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 593
---

# REL08-BP02 Integrate functional testing as part of your deployment

Use techniques such as unit tests and integration tests that validate required functionality.
Unit testing is the process where you test the smallest functional unit of code to validate its
behavior. Integration testing seeks to validate that each application feature works according to
the software requirements. While unit tests focus on testing part of an application in isolation,
integration tests consider side effects (for example, the effect of data being changed through a
mutation operation). In either case, tests should be integrated into a deployment pipeline, and
if success criteria are not met, the pipeline is halted or rolled back. These tests are run in a pre-
production environment, which is staged prior to production in the pipeline.
You achieve the best outcomes when these tests are run automatically as part of build and
deployment actions. For instance, with AWS CodePipeline, developers commit changes to a source
repository where CodePipeline automatically detects the changes. The application is built, and
unit tests are run. After the unit tests have passed, the built code is deployed to staging servers for
testing. From the staging server, CodePipeline runs more tests, such as integration or load tests.
Upon the successful completion of those tests, CodePipeline deploys the tested and approved code
to production instances.
Desired outcome: You use automation to perform unit and integration tests to validate that your
code behaves as expected. These tests are integrated into the deployment process, and a test
failure aborts the deployment.
