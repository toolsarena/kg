---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 840
---

# Implementation guidance

AWS Organizations allows you to create multiple AWS accounts which can help you centrally
govern your environment as you scale your workloads on AWS. You can model your organizational
hierarchy by grouping AWS accounts in organizational unit (OU) structure and creating multiple
AWS accounts under each OU. To create an account structure, you need to decide which of your
AWS accounts will be the management account first. After that, you can create new AWS accounts
or select existing accounts as member accounts based on your designed account structure by
following management account best practices and member account best practices.
