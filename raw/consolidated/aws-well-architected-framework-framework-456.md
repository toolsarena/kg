---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 597
---

# AWS Well-Architected Framework Framework

• Once your DR plans and SOPs are updated, complete disaster recovery testing to verify that they
are effective. Disaster recovery testing helps you determine if you can restore your system after
an event and return to normal operations. You can simulate various disaster recovery strategies
and identify whether your planning is sufficient to meet your uptime requirements. Common
disaster recovery strategies include backup and restore, pilot light, cold standby, warm standby,
hot standby, and active-active, and they all differ in cost and complexity. Before disaster recovery
testing, we recommend that you define your recovery time objective (RTO) and recovery point
objective (RPO) to simplify the choice of strategy to simulate. AWS offers disaster recovery tools
like AWS Elastic Disaster Recovery to help you get started with your planning and testing.
• Chaos engineering experiments introduce disruptions to the system, such as network outages
and service failures. By simulating with controlled failures, you can discover your system's
vulnerabilities while containing the impacts of the injected failures. Just like the other strategies,
run controlled failure simulations in non-production environments using services like AWS Fault
Injection Service to gain confidence before deploying in production.


# AWS Well-Architected Framework Framework

Level of risk exposed if this best practice is not established: Medium

# AWS Well-Architected Framework Framework

Figure 8: Blue/green deployment with AWS Elastic Beanstalk and Amazon Route 53