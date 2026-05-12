---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 601
---

# AWS Well-Architected Framework Framework

• AWS Elastic Beanstalk is a service to rapidly deploy and scale web applications developed
with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as
Apache, NGINX, Passenger, and IIS.
• AWS Proton helps platform teams connect and coordinate all the different tools your
development teams need for infrastructure provisioning, code deployments, monitoring,
and updates. AWS Proton enables automated infrastructure as code provisioning and
deployment of serverless and container-based applications.
• Leveraging infrastructure as code makes it easy to automate infrastructure deployment, and
helps achieve infrastructure immutability. AWS provides services that enable the creation,
deployment, and maintenance of infrastructure in a programmatic, descriptive, and declarative
way.
• AWS CloudFormation helps developers create AWS resources in an orderly and predictable
fashion. Resources are written in text files using JSON or YAML format. The templates
require a specific syntax and structure that depends on the types of resources being created
and managed. You author your resources in JSON or YAML with any code editor, check it
into a version control system, and then CloudFormation builds the specified services in safe,
repeatable manner.
• AWS Serverless Application Model (AWS SAM) is an open-source framework that you can use
to build serverless applications on AWS. AWS SAM integrates with other AWS services, and is
an extension of CloudFormation.
• AWS Cloud Development Kit (AWS CDK) is an open-source software development framework
to model and provision your cloud application resources using familiar programming
languages. You can use AWS CDK to model application infrastructure using TypeScript,
Python, Java, and .NET. AWS CDK uses CloudFormation in the background to provision
resources in a safe, repeatable manner.
• AWS Cloud Control API introduces a common set of Create, Read, Update, Delete, and
List (CRUDL) APIs to help developers manage their cloud infrastructure in an easy and
consistent way. The Cloud Control API common APIs allow developers to uniformly manage
the lifecycle of AWS and third-party services.
• Implement deployment patterns that minimize user impact.
• Canary deployments:
• Set up an API Gateway canary release deployment
• Create a pipeline with canary deployments for Amazon ECS using AWS App Mesh
