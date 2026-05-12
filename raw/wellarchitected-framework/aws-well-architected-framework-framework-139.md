---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 183
---

# AWS Well-Architected Framework Framework

• Your release is comprised of application, infrastructure, patches and configuration updates that
are independent from one another. However, you have a single CI/CD pipeline that delivers
all changes at once. A failure in one component forces you to revert all changes, making your
rollback complex and inefficient.
• Your team completes the coding work in sprint one and begins sprint two work, but your plan
did not include testing until sprint three. As a result, automated tests revealed defects from
sprint one that had to be resolved before testing of sprint two deliverables could be started and
the entire release is delayed, devaluing your automated testing.
• Your automated regression test cases for the production release are complete, but you are not
monitoring workload health. Since you have no visibility into whether or not the service has
restarted, you are not sure if rollback is needed or if it has already occurred.
Benefits of establishing this best practice: Automated testing increases the transparency of your
testing process and your ability to cover more features in a shorter time period. By testing and
validating changes in production, you are able to identify issues immediately. Improvement in
consistency with automated testing tools allows for better detection of defects. By automatically
rolling back to the previous version, the impact on your customers is minimized. Automated
rollback ultimately inspires more confidence in your deployment capabilities by reducing business
impact. Overall, these capabilities reduce time-to-delivery while ensuring quality.
Level of risk exposed if this best practice is not established: Medium
