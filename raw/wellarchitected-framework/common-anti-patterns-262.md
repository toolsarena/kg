---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 182
---

# Common anti-patterns:

• Your systems are not architected in a way that allows them to be updated with smaller releases.
As a result, you have difficulty in reversing those bulk changes during a failed deployment.
• Your deployment process consists of a series of manual steps. After you deploy changes to your
workload, you start post-deployment testing. After testing, you realize that your workload is
inoperable and customers are disconnected. You then begin rolling back to the previous version.
All of these manual steps delay overall system recovery and cause a prolonged impact to your
customers.
• You spent time developing automated test cases for functionality that is not frequently used in
your application, minimizing the return on investment in your automated testing capability.
