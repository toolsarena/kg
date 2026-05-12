---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 834
---

# Implementation steps

• Meet with stakeholders: To develop policies, ask stakeholders (cloud business office, engineers,
or functional decision makers for policy enforcement) within your organization to specify
their requirements and document them. Take an iterative approach by starting broadly and
continually refine down to the smallest units at each step. Team members include those with
direct interest in the workload, such as organization units or application owners, as well as
supporting groups, such as security and finance teams.
• Get confirmation: Make sure teams agree on policies who can access and deploy to the AWS
Cloud. Make sure they follow your organization’s policies and confirm that their resource
creations align with the agreed policies and procedures.
• Create onboarding training sessions: Ask new organization members to complete onboarding
training courses to create cost awareness and organization requirements. They may assume
different policies from their previous experience or not think of them at all.
• Define locations for your workload: Define where your workload operates, including the
country and the area within the country. This information is used for mapping to AWS Regions
and Availability Zones.
• Define and group services and resources: Define the services that the workloads require. For
each service, specify the types, the size, and the number of resources required. Define groups for
the resources by function, such as application servers or database storage. Resources can belong
to multiple groups.
• Define and group the users by function: Define the users that interact with the workload,
focusing on what they do and how they use the workload, not on who they are or their position
in the organization. Group similar users or functions together. You can use the AWS managed
policies as a guide.
• Define the actions: Using the locations, resources, and users identified previously, define
the actions that are required by each to achieve the workload outcomes over its life time
