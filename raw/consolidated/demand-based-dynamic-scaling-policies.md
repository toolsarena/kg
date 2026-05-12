---
title: "Demand-based dynamic scaling policies"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 922
---

# Demand-based dynamic scaling policies

• Simple/Step Scaling: Monitors metrics and adds/removes instances as per steps defined by the
customers manually.
• Target Tracking: Thermostat-like control mechanism that automatically adds or removes
instances to maintain metrics at a customer defined target.
When architecting with a demand-based approach keep in mind two key considerations. First,
understand how quickly you must provision new resources. Second, understand that the size of
margin between supply and demand will shift. You must be ready to cope with the rate of change
in demand and also be ready for resource failures.
Time-based supply: A time-based approach aligns resource capacity to demand that is predictable
or well-defined by time. This approach is typically not dependent upon utilization levels of the
resources. A time-based approach ensures that resources are available at the specific time they
are required and can be provided without any delays due to start-up procedures and system or
consistency checks. Using a time-based approach, you can provide additional resources or increase
capacity during busy periods.


# Demand or Spot Instances

based on your job requireme
nts

# Demand or Spot Instances

based on your job requireme
nts