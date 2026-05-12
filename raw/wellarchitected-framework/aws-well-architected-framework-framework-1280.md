---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 682
---

# AWS Well-Architected Framework Framework

6. What are the recovery objectives and availability expectations of workloads that depend on
this one (upstream)? Upstream workload objectives may require this workload to have more
stringent recovery capabilities than it first appears.
7. Are there different recovery objectives based on the type of incident? For example, you might
have different RTOs and RPOs depending on whether the incident impacts an Availability Zone
or an entire Region.
8. Do your recovery objectives change during certain events or times of the year? For example, you
might have different RTOs and RPOs around holiday shopping seasons, sporting events, special
sales, and new product launches.
9. How do the recovery objectives align with any line of business and organizational disaster
recovery strategy you might have?
10.Are there legal or contractual ramifications to consider? For example, are you contractually
obligated to provide a service with a given RTO or RPO? What penalties might you incur for not
meeting them?
11.Are you required to maintain data integrity to meet regulatory or compliance requirements?
The following worksheet can aid your evaluation of each workload. You may modify this worksheet
to suit your specific needs, such as adding additional questions.
