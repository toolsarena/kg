---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 386
---

# Implementation guidance

You can apply the automations described in the Security Pillar practices for protecting your
compute resources. SEC06-BP01 Perform vulnerability management describes how you can
use Amazon Inspector in both your CI/CD pipelines and for continually scanning your runtime
environments for known Common Vulnerabilities and Exposures (CVEs). You can use AWS Systems
Manager to apply patches or redeploy from fresh images through automated runbooks to keep
your compute fleet updated with the latest software and libraries. Use these techniques to reduce
the need for manual processes and interactive access to your compute resources. See SEC06-BP03
Reduce manual management and interactive access to learn more.
Automation also plays a role in deploying workloads that are trustworthy, described in SEC06-
BP02 Provision compute from hardened images and SEC06-BP04 Validate software integrity. You
can use services such as EC2 Image Builder, AWS Signer, AWS CodeArtifact, and Amazon Elastic
Container Registry (ECR) to download, verify, construct, and store hardened and approved images
and code dependencies. Alongside Inspector, each of these can play a role in your CI/CD process
so your workload makes its way to production only when it is confirmed that its dependencies are
up-to-date and from trusted sources. Your workload is also signed so AWS compute environments,
such as AWS Lambda and Amazon Elastic Kubernetes Service (EKS) can verify it hasn't been
tampered with before allowing it to run.
Beyond these preventative controls, you can use automation in your detective controls for your
compute resources as well. As one example, AWS Security Hub CSPM offers the NIST 800-53 Rev. 5
standard that includes checks such as [EC2.8] EC2 instances should use Instance Metadata Service
Version 2 (IMDSv2). IMDSv2 uses the techniques of session authentication, blocking requests that
contain an X-Forwarded-For HTTP header, and a network TTL of 1 to stop traffic originating from
external sources to retrieve information about the EC2 instance. This check in Security Hub CSPM
can detect when EC2 instances use IMDSv1 and initiate automated remediation. Learn more about
automated detection and remediations in SEC04-BP04 Initiate remediation for non-compliant
resources.
