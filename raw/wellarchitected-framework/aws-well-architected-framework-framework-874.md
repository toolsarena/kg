---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 160
---

# AWS Well-Architected Framework Framework

upcoming changes and updates that should be performed. Major planned lifecycle events are sent
at least six months in advance.
Amazon EC2 Image Builder provides pipelines to update machine images. As a part of patch
management, consider Amazon Machine Images (AMIs) using an AMI image pipeline or container
images with a Docker image pipeline, while AWS Lambda provides patterns for custom runtimes
and additional libraries to remove vulnerabilities.
You should manage updates to Amazon Machine Images for Linux or Windows Server images using
Amazon EC2 Image Builder. You can use Amazon Elastic Container Registry (Amazon ECR) with
your existing pipeline to manage Amazon ECS images and manage Amazon EKS images. Lambda
includes version management features.
Patching should not be performed on production systems without first testing in a safe
environment. Patches should only be applied if they support an operational or business outcome.
On AWS, you can use AWS Systems Manager Patch Manager to automate the process of patching
managed systems and schedule the activity using Systems Manager Maintenance Windows.
Desired outcome: Your AMI and container images are patched, up-to-date, and ready for launch.
You are able to track the status of all deployed images and know patch compliance. You are able to
report on current status and have a process to meet your compliance needs.
