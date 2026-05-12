---
title: "Customer example"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 152
---

# Customer example

As part of their continuous integration pipeline, AnyCompany Retail conducts several types of tests
on all software artifacts. They practice test driven development so all software has unit tests. Once
the artifact is built, they run end-to-end tests. After this first round of tests is complete, they run a
static application security scan, which looks for known vulnerabilities. Developers receive messages
as each testing gate is passed. Once all tests are complete, the software artifact is stored in an
artifact repository.
