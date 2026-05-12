---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 677
---

# Implementation guidance

Once you have designed and implemented the necessary resilience measures, conduct a game day
to validate that everything works as planned in production. A game day, especially the first one,
should involve all team members, and all stakeholders and participants should be informed in
advance about the date, time, and simulated scenarios.
During the game day, the involved teams simulate various events and potential scenarios according
to the prescribed procedures. The participants closely monitor and assess the impact of these
simulated events. If the system operates as designed, the automated detection, scaling, and self-
healing mechanisms should activate and result in little to no impact on users. If the team observes
any negative impact, they roll back the test and remedy the identified issues, either through
automated means or manual intervention documented in the applicable runbooks.
To continuously improve resilience, it's critical to document and incorporate lessons learned. This
process is a feedback loop that systematically captures insights from game days and uses them to
enhance systems, processes, and team capabilities.
