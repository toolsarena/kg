---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 278
---

# Implementation guidance

Review trusted threat intelligence publications to stay on top of the threat landscape. Consult
the MITRE ATT&CK knowledge base for documentation on known adversarial tactics, techniques,
and procedures (TTPs). Review MITRE's Common Vulnerabilities and Exposures (CVE) list to
stay informed on known vulnerabilities in products you rely on. Understand critical risks to web
applications with the Open Worldwide Application Security Project (OWASP)'s popular OWASP Top
10 project.
Stay up to date on AWS security events and recommended remediation steps with AWS Security
Bulletins for CVEs.
To reduce your overall effort and overhead of staying up to date, consider using AWS services that
automatically incorporate new threat intelligence over time. For example, Amazon GuardDuty
stays up to date with industry threat intelligence for detecting anomalous behaviors and threat
signatures within your accounts. Amazon Inspector automatically keeps a database of the CVEs
it uses for its continuous scanning features up to date. Both AWS WAF and AWS Shield Advanced
provide managed rule groups that are updated automatically as new threats emerge.
Review the Well-Architected operational excellence pillar for automated fleet management and
patching.
