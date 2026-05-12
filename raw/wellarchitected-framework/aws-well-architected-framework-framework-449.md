---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 589
---

# AWS Well-Architected Framework Framework

3. Select the appropriate automatic scaling mechanism for the component. For Amazon EC2
instances, use Amazon EC2 Auto Scaling. For other AWS services, use Application Auto Scaling.
For Kubernetes pods (such as those running in an Amazon EKS cluster), consider Horizontal Pod
Autoscaler (HPA) or Kubernetes Event-driven Autoscaling (KEDA). For Kubernetes or EKS nodes,
consider Karpenter and Cluster Auto Scaler (CAS).
4. For metric or scheduled scaling, conduct load testing to determine the appropriate scaling
metrics and target values for your workload. For scheduled scaling, determine the number
of resources needed at the dates and times you select. Determine the maximum number of
resources needed to serve expected peak traffic.
5. Configure the auto scaler based on the information collected above. Consult the auto scaling
service's documentation for details. Verify that the maximum and minimum scaling limits are
configured correctly.
6. Verify the scaling configuration is working as expected. Perform load testing in a non-
production environment and observe how the system reacts, and adjust as needed. When
enabling auto scaling in production, configure appropriate alarms to notify you of any
unexpected behavior.
