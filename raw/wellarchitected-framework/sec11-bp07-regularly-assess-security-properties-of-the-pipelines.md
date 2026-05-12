---
title: "SEC11-BP07 Regularly assess security properties of the pipelines"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 465
---

# SEC11-BP07 Regularly assess security properties of the pipelines

Apply the principles of the Well-Architected Security Pillar to your pipelines, with particular
attention to the separation of permissions. Regularly assess the security properties of your pipeline
infrastructure. Effectively managing the security of the pipelines allows you to deliver the security
of the software that passes through the pipelines.
Desired outcome: The pipelines you use to build and deploy your software follow the same
recommended practices as any other workload in your environment. The tests that you implement
in your pipelines are not editable by the teams who use them. You give the pipelines only the
permissions needed for the deployments they are doing using temporary credentials. You
implement safeguards to prevent pipelines from deploying to the wrong environments. You
configure your pipelines to emit state so that the integrity of your build environments can be
validated.
