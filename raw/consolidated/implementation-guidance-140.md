---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 530
---

# Implementation guidance

• Do constant work so that systems do not fail when there are large, rapid changes in load.
• Implement loosely coupled dependencies. Dependencies such as queuing systems, streaming
systems, workflows, and load balancers are loosely coupled. Loose coupling helps isolate
behavior of a component from other components that depend on it, increasing resiliency and
agility.
• The Amazon Builders' Library: Reliability, constant work, and a good cup of coffee
• AWS re:Invent 2018: Close Loops and Opening Minds: How to Take Control of Systems, Big and
