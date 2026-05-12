---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 466
---

# AWS Well-Architected Framework Framework

Verify that the teams responsible for building and deploying applications do not have the ability
to edit or bypass the security tests and checks implemented in your pipelines. This separation of
concerns helps maintain the integrity of your build and deployment processes.
As a starting point, consider employing the AWS Deployment Pipelines Reference Architecture. This
reference architecture provides a secure and scalable foundation for building your CI/CD pipelines
on AWS.
Additionally, you can use services like AWS Identity and Access Management Access Analyzer to
generate least-privilege IAM policies for both your pipeline permissions and as a step in your
pipeline to verify workload permissions. This helps verify that your pipelines and workloads have
only the necessary permissions required for their specific functions, which reduces the risk of
unauthorized access or actions.
