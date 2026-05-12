---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 323
---

# Common anti-patterns:

• You do not have well-documented and well-tested emergency access processes. Your users are
unprepared for an emergency and follow improvised processes when an emergency event arises.
• Your emergency access processes depend on the same systems (such as a centralized identity
provider) as your normal access mechanisms. This means that the failure of such a system may
impact both your normal and emergency access mechanisms and impair your ability to recover
from the failure.
• Your emergency access processes are used in non-emergency situations. For example, your users
frequently misuse emergency access processes as they find it easier to make changes directly
than submit changes through a pipeline.
• Your emergency access processes do not generate sufficient logs to audit the processes, or the
logs are not monitored to alert for potential misuse of the processes.
