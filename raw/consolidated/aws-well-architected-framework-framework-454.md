---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 595
---

# AWS Well-Architected Framework Framework

4. Set up your source, build, test, and deploy stages using the AWS CodePipeline console or AWS
Command Line Interface (CLI).
5. Deploy the application once the code has been built and tested. AWS CodeDeploy can deploy
it to your staging (testing) and production environments. These environments may include
Amazon EC2 instances, AWS Lambda functions, or on-premises servers. The same deployment
mechanism should be used to deploy the application to all environments.
6. Monitor the progress of your pipeline and the status of each stage. Use quality checks to block
the pipeline based on the status of your tests. You can also receive notifications for any pipeline
stage failure or pipeline completion.
7. Continually monitor the results of the tests, and look for patterns, regressions or areas that
require more attention. Use this information to improve the test suite, identify areas of the
application that need more robust testing, and optimize the deployment process.
