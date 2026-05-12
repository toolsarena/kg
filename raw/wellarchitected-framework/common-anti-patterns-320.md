---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 378
---

# Common anti-patterns:

• Acquiring images and libraries from trusted registries, but not verifying their signature or
performing vulnerability scans before putting into use.
• Hardening images, but not regularly testing them for new vulnerabilities or updating to the
latest version.
• Installing or not removing software packages that are not required during the expected lifecycle
of the image.
• Relying solely on patching to keep production compute resources up to date. Patching alone can
still cause compute resources to drift from the hardened standard over time. Patching can also
fail to remove malware that may have been installed by a threat actor during a security event.
Benefits of establishing this best practice: Hardening images helps reduce the number of paths
available in your runtime environment that can allow unintended access to unauthorized users or
services. It also can reduce the scope of impact should any unintended access occur.
Level of risk exposed if this best practice is not established: High
