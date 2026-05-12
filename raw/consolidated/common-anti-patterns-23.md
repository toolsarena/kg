---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 157
---

# Common anti-patterns:

• After compiling your code on your development system, you copy the executable onto your
production systems and it fails to start. The local log files indicates that it has failed due to
missing dependencies.
• You successfully build your application with new features in your development environment and
provide the code to quality assurance (QA). It fails QA because it is missing static assets.
• On Friday, after much effort, you successfully built your application manually in your
development environment including your newly coded features. On Monday, you are unable to
repeat the steps that allowed you to successfully build your application.
