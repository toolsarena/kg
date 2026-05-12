---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 452
---

# AWS Well-Architected Framework Framework

• Consider where in the SDLC it is appropriate to block pipelines instead of just notifying builders
that issues need to be remediated.
• Automated Security Helper (ASH) is an example for open-source code security scanning tool.
• Performing testing or code analysis using automated tools, such as Amazon Q Developer
integrated with developer IDEs, and Amazon CodeGuru Security for scanning code on commit,
helps builders get feedback at the right time.
• When building using AWS Lambda, you can use Amazon Inspector to scan the application code in
your functions.
• When automated testing is included in CI/CD pipelines, you should use a ticketing system to
track the notification and remediation of software issues.
• For security tests that might generate findings, linking to guidance for remediation helps
builders improve code quality.
• Regularly analyze the findings from automated tools to prioritize the next automation, builder
training, or awareness campaign.
• To extract SBOM as part of your CI/CD pipelines, use Amazon Inspector SBOM Generator to
produce SBOMs for archives, container images, directories, local systems, and compiled Go and
Rust binaries in the CycloneDX SBOM format.


# AWS Well-Architected Framework Framework

• How AWS approaches automating safe, hands-off deployments
• How Amazon CodeGuru Security helps you effectively balance security and velocity