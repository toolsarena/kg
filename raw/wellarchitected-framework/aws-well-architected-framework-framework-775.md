---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 34
---

# AWS Well-Architected Framework Framework

• Detailed logging that contains important content, such as file access and changes, is available.
• AWS has designed storage systems for exceptional resiliency. For example, Amazon S3
Standard, S3 Standard–IA, S3 One Zone-IA, and Amazon Glacier are all designed to provide
99.999999999% durability of objects over a given year. This durability level corresponds to an
average annual expected loss of 0.000000001% of objects.
• Versioning, which can be part of a larger data lifecycle management process, can protect against
accidental overwrites, deletes, and similar harm.
• AWS never initiates the movement of data between Regions. Content placed in a Region will
remain in that Region unless you explicitly use a feature or leverage a service that provides that
functionality.
The following questions focus on these considerations for security.
SEC 7: How do you classify your data?
Classification provides a way to categorize data, based on criticality and sensitivity in order to
help you determine appropriate protection and retention controls.
SEC 8: How do you protect your data at rest?
Protect your data at rest by implementing multiple controls, to reduce the risk of unauthorized
access or mishandling.
SEC 9: How do you protect your data in transit?
Protect your data in transit by implementing multiple controls to reduce the risk of unauthori
zed access or loss.
AWS provides multiple means for encrypting data at rest and in transit. We build features into our
services that make it easier to encrypt your data. For example, we have implemented server-side
encryption (SSE) for Amazon S3 to make it easier for you to store your data in an encrypted form.
You can also arrange for the entire HTTPS encryption and decryption process (generally known as
SSL termination) to be handled by Elastic Load Balancing (ELB).
