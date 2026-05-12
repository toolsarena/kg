---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 150
---

# Common anti-patterns:

• You have been developing and storing your code on your workstation. You have had an
unrecoverable storage failure on the workstation and your code is lost.
• After overwriting the existing code with your changes, you restart your application and it is no
longer operable. You are unable to revert the change.
• You have a write lock on a report file that someone else needs to edit. They contact you asking
that you stop work on it so that they can complete their tasks.
• Your research team has been working on a detailed analysis that shapes your future work.
Someone has accidentally saved their shopping list over the final report. You are unable to revert
the change and have to recreate the report.
Benefits of establishing this best practice: By using version control capabilities you can easily
revert to known good states and previous versions, and limit the risk of assets being lost.
Level of risk exposed if this best practice is not established: High
