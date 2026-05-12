---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 142
---

# Implementation steps

1. Deploy Amazon CloudWatch RUM: Integrate your application with CloudWatch RUM to collect,
analyze, and present real user data.
a. Use the CloudWatch RUM JavaScript library to integrate RUM with your application.
b. Set up dashboards to visualize and monitor real user data.
2. Configure CloudWatch Synthetics: Create canaries, or scripted routines, that simulate user
interactions with your application.
a. Define critical application workflows and paths.
b. Design canaries using CloudWatch Synthetics scripts to simulate user interactions for these
paths.
c. Schedule and monitor canaries to run at specified intervals, ensuring consistent performance
checks.
3. Analyze and act on data: Utilize data from RUM and synthetic transactions to gain insights and
take corrective measures when anomalies are detected. Use CloudWatch dashboards and alarms
to stay informed.
