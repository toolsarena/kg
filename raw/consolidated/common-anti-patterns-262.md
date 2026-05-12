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


# Common anti-patterns:

• Deploying a workload without team members trained to operate the platform and services in
use.
• Not having enough personnel to support on-call rotations or personnel taking time off.

# Common anti-patterns:

• You launch a workload without knowing if you can operate it.
• Governance and security requirements are not included in certifying a workload for launch.
• Workloads are not re-evaluated periodically.
• Workloads launch without required procedures in place.

# Common anti-patterns:

• Relying on memory to complete each step of a process.
• Manually deploying changes without a checklist.
• Different team members performing the same process but with different steps or outcomes.
• Letting runbooks drift out of sync with system changes and automation.