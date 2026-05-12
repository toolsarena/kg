---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 384
---

# AWS Well-Architected Framework Framework

If you are using a downloaded software or artifacts in your workload, check if the provider provides
a public key for digital signature verification. Here are some examples of how AWS provides a
public key and verification instructions for software we publish:
• EC2 Image Builder: Verify the signature of the AWSTOE installation download
• AWS Systems Manager: Verifying the signature of SSM Agent
• Amazon CloudWatch: Verifying the signature of the CloudWatch agent package
Incorporate digital signature verification into the processes you use for obtaining and hardening
images, as discussed in SEC06-BP02 Provision compute from hardened images.
You can use AWS Signer to help manage the verification of signatures, as well as your own code-
signing lifecycle for your own software and artifacts. Both AWS Lambda and Amazon Elastic
Container Registry provide integrations with Signer to verify the signatures of your code and
images. Using the examples in the Resources section, you can incorporate Signer into your
continuous integration and delivery (CI/CD) pipelines to automate verification of signatures and
the signing of your own code and images.
