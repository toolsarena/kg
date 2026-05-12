---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 971
---

# Implementation steps

• For fixed size storage like Amazon EBS, verify that you are monitoring the amount of storage
used versus the overall storage size and create automation, if possible, to increase the storage
size when reaching a threshold.
• Use elastic volumes and managed block data services to automate allocation of additional
storage as your persistent data grows. As an example, you can use Amazon EBS Elastic Volumes
to change volume size, volume type, or adjust the performance of your Amazon EBS volumes.
