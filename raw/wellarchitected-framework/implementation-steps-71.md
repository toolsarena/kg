---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 379
---

# Implementation steps

• Harden operating systems. Use base images from trusted sources as a foundation for building
your hardened AMIs. Use EC2 Image Builder to help customize the software installed on your
images.
• Harden containerized resources. Configure containerized resources to meet security best
practices. When using containers, implement ECR Image Scanning in your build pipeline and on a
regular basis against your image repository to look for CVEs in your containers.
• When using serverless implementation with AWS Lambda, use Lambda layers to segregate
application function code and shared dependent libraries. Configure code signing for Lambda to
make sure that only trusted code runs in your Lambda functions.
