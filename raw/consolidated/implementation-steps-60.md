---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 338
---

# Implementation steps

• Consider using AWS Config for AWS Organizations: AWS Config allows you to aggregate
findings from multiple accounts within an AWS Organizations to a delegated administrator
account. This provides a comprehensive view, and allows you to deploy AWS Config Rules across
accounts to detect publicly accessible resources.


# Implementation steps

1. Use AWS Organizations: AWS Organizations is an account management service that allows
you to consolidate multiple AWS accounts into an organization that you create and centrally
manage. You can group your accounts into organizational units (OUs) and attach different