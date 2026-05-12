---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 451
---

# Implementation guidance

As you build your software, adopt various mechanisms for software testing to ensure that you are
testing your application for both functional requirements, based on your application’s business
logic, and non-functional requirements, which are focused on application reliability, performance,
and security.
Static application security testing (SAST) analyzes your source code for anomalous security
patterns, and provides indications for defect prone code. SAST relies on static inputs, such as
documentation (requirements specification, design documentation, and design specifications)
and application source code to test for a range of known security issues. Static code analyzers
can help expedite the analysis of large volumes of code. The NIST Quality Group provides a
comparison of Source Code Security Analyzers, which includes open source tools for Byte Code
Scanners and Binary Code Scanners.
Complement your static testing with dynamic analysis security testing (DAST) methodologies,
which performs tests against the running application to identify potentially unexpected behavior.
Dynamic testing can be used to detect potential issues that are not detectable via static analysis.
Testing at the code repository, build, and pipeline stages allows you to check for different
types of potential issues from entering into your code. Amazon Q Developers provides code
recommendations, including security scanning, in the builder's IDE. Amazon CodeGuru Security can
identify critical issues, security issues, and hard-to-find bugs during application development, and
provides recommendations to improve code quality. Extracting Software Bill of Materials (SBOM)
also allows you to extract a formal record containing the details and relationships of the various
components used in building your software. This allows you to inform vulnerability management,
and quickly identify software or component dependencies and supply chain risks.
The Security for Developers workshop uses AWS developer tools, such as AWS CodeBuild, AWS
CodeCommit, and AWS CodePipeline, for release pipeline automation that includes SAST and DAST
testing methodologies.
As you progress through your SDLC, establish an iterative process that includes periodic application
reviews with your security team. Feedback gathered from these security reviews should be
addressed and validated as part of your release readiness review. These reviews establish a robust
application security posture, and provide builders with actionable feedback to address potential
issues.
