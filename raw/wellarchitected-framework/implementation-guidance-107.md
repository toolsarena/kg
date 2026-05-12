---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 409
---

# Implementation guidance

Protecting data at rest is important to maintain data integrity, confidentiality, and compliance
with regulatory requirements. You can implement multiple controls to help achieve this, including
access control, isolation, conditional access, and versioning.
You can enforce access control with the principle of least privilege, which provides only the
necessary permissions to users and services to perform their tasks. This includes access to
encryption keys. Review your AWS Key Management Service (AWS KMS) policies to verify that the
level of access you grant is appropriate and that relevant conditions apply.
You can separate data based on different classification levels by using distinct AWS accounts for
each level, and manage these accounts using AWS Organizations. This isolation can help prevent
unauthorized access and minimizes the risk of data exposure.
Regularly review the level of access granted in Amazon S3 bucket policies. Avoid using publicly
readable or writeable buckets unless absolutely necessary. Consider using AWS Config to detect
publicly available buckets and Amazon CloudFront to serve content from Amazon S3. Verify that
buckets that should not allow public access are properly configured to prevent it.
Implement versioning and object locking mechanisms for critical data stored in Amazon S3.
Amazon S3 versioning preserves previous versions of objects to recover data from accidental
