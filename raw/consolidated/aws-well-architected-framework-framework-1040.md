---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 379
---

# AWS Well-Architected Framework Framework

software, and then incrementally apply CIS controls to test their impact. For any CIS control that
prevents your software from running, test if you can implement the finer-grained hardening
recommendations in a DISA instead. Keep track of the different CIS controls and DISA STIG
configurations you are able to apply successfully. Use these to define your image hardening recipes
in EC2 Image Builder accordingly.
For containerized workloads, hardened images from Docker are available on the Amazon Elastic
Container Registry (ECR) public repository. You can use EC2 Image Builder to harden container
images alongside AMIs.
Similar to operating systems and container images, you can obtain code packages (or libraries)
from public repositories, through tooling such as pip, npm, Maven, and NuGet. We recommend you
manage code packages by integrating private repositories, such as within AWS CodeArtifact, with
trusted public repositories. This integration can handle retrieving, storing, and keeping packages
up-to-date for you. Your application build processes can then obtain and test the latest version of
these packages alongside your application, using techniques like Software Composition Analysis
(SCA), Static Application Security Testing (SAST), and Dynamic Application Security Testing (DAST).
For serverless workloads that use AWS Lambda, simplify managing package dependencies using
Lambda layers. Use Lambda layers to configure a set of standard dependencies that are shared
across different functions into a standalone archive. You can create and maintain layers through
their own build process, providing a central way for your functions to stay up-to-date.


# AWS Well-Architected Framework Framework

• OPS05-BP05 Perform patch management