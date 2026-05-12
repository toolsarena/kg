---
title: "SEC03-BP03 Establish emergency access process"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 322
---

# SEC03-BP03 Establish emergency access process

Create a process that allows for emergency access to your workloads in the unlikely event of an
issue with your centralized identity provider.
You must design processes for different failure modes that may result in an emergency event.
For example, under normal circumstances, your workforce users federate to the cloud using a
centralized identity provider (SEC02-BP04) to manage their workloads. However, if your centralized
identity provider fails, or the configuration for federation in the cloud is modified, then your
workforce users may not be able to federate into the cloud. An emergency access process allows
authorized administrators to access your cloud resources through alternate means (such as an
alternate form of federation or direct user access) to fix issues with your federation configuration
or your workloads. The emergency access process is used until the normal federation mechanism is
restored.
