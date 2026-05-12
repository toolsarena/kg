---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 141
---

# Common anti-patterns:

• Applications without real user monitoring (RUM):
• Delayed issue detection: Without RUM, you might not become aware of performance
bottlenecks or issues until users complain. This reactive approach can lead to customer
dissatisfaction.
• Lack of user experience insights: Not using RUM means you lose out on crucial data that
shows how real users interact with your application, limiting your ability to optimize the user
experience.
• Applications without synthetic transactions:
• Missed edge cases: Synthetic transactions help you test paths and functions that might not be
frequently used by typical users but are critical to certain business functions. Without them,
these paths could malfunction and go unnoticed.
• Checking for issues when the application is not being used: Regular synthetic testing can
simulate times when real users aren't actively interacting with your application, ensuring the
system always functions correctly.
