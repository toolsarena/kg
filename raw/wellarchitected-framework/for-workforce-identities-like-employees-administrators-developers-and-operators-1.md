---
title: "For workforce identities like employees, administrators, developers, and operators:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 295
---

# For workforce identities like employees, administrators, developers, and operators:

• You should rely on a centralized identity provider and require human users to use federation with
an identity provider to access AWS using temporary credentials. Federation for your users can be
done either with direct federation to each AWS account or using AWS IAM Identity Center and
the identity provider of your choice. Federation provides a number of advantages over using IAM
users in addition to eliminating long-term credentials. Your users can also request temporary
credentials from the command line for direct federation or by using IAM Identity Center. This
means that there are few uses cases that require IAM users or long-term credentials for your
users.
