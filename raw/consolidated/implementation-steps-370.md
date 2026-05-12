---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 585
---

# Implementation steps

• Define the procedures, manual or automated, that scale the required resources.
• Scaling procedures depend on how the different components within your workload are
designed.
• Scaling procedures also vary depending on the underlying technology utilized.
• Components using AWS Auto Scaling can use scaling plans to configure a set of instructions
for scaling your resources. If you work with AWS CloudFormation or add tags to AWS
resources, you can set up scaling plans for different sets of resources per application. Auto
Scaling provides recommendations for scaling strategies customized to each resource. After
you create your scaling plan, Auto Scaling combines dynamic scaling and predictive scaling
methods together to support your scaling strategy. For more detail, see How scaling plans
work.
• Amazon EC2 Auto Scaling verifies that you have the correct number of Amazon EC2
instances available to handle the load for your application. You create collections of EC2
instances, called Auto Scaling groups. You can specify the minimum and maximum number
of instances in each Auto Scaling group, and Amazon EC2 Auto Scaling ensures that your
group never goes below or above these limits. For more detail, see What is Amazon EC2
Auto Scaling?
• Amazon DynamoDB auto scaling uses the Application Auto Scaling service to dynamically
adjust provisioned throughput capacity on your behalf, in response to actual traffic patterns.
This allows a table or a global secondary index to increase its provisioned read and write
capacity to handle sudden increases in traffic, without throttling. For more detail, see
Managing throughput capacity automatically with DynamoDB auto scaling.


# Implementation steps

1. Determine whether the workload component is suitable for automatic scaling.
2. Determine what kind of scaling mechanism is most appropriate for the workload: metric-based
scaling, scheduled scaling, or predictive scaling.