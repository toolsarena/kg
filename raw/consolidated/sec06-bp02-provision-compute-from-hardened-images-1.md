---
title: "SEC06-BP02 Provision compute from hardened images"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 377
---

# SEC06-BP02 Provision compute from hardened images

Provide fewer opportunities for unintended access to your runtime environments by deploying
them from hardened images. Only acquire runtime dependencies, such as container images and
application libraries, from trusted registries and verify their signatures. Create your own private
registries to store trusted images and libraries for use in your build and deploy processes.
Desired outcome: Your compute resources are provisioned from hardened baseline images. You
retrieve external dependencies, such as container images and application libraries, only from
trusted registries and verify their signatures. These are stored in private registries for your build
