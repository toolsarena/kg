---
title: "5. Implement versioning and object locking mechanisms:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 410
---

# 5. Implement versioning and object locking mechanisms:

• Use Amazon S3 versioning to preserve previous versions of objects, which provides recovery
from accidental deletion or overwrites.
• Use Amazon S3 Object Lock to provide mandatory access control for objects, which prevents
them from being deleted or overwritten, even by the root user, until the lock expires.
• Use Amazon Glacier Vault Lock for archives stored in Amazon Glacier.
6Da.taU psroete Actimonazon S3 Inventory: 405
