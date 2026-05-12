---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 854
---

# Implementation guidance

Implement tagging in AWS to add organization information to your resources, which will then be
added to your cost and usage information. A tag is a key-value pair — the key is defined and must
be unique across your organization, and the value is unique to a group of resources. An example
of a key-value pair is the key is Environment, with a value of Production. All resources in the
production environment will have this key-value pair. Tagging allows you categorize and track
your costs with meaningful, relevant organization information. You can apply tags that represent
organization categories (such as cost centers, application names, projects, or owners), and identify
workloads and characteristics of workloads (such as test or production) to attribute your costs and
usage throughout your organization.
When you apply tags to your AWS resources (such as Amazon Elastic Compute Cloud instances
or Amazon Simple Storage Service buckets) and activate the tags, AWS adds this information to
your Cost and Usage Reports. You can run reports and perform analysis on tagged and untagged
resources to allow greater compliance with internal cost management policies and ensure accurate
attribution.
Creating and implementing an AWS tagging standard across your organization’s accounts helps you
manage and govern your AWS environments in a consistent and uniform manner. Use Tag Policies
in AWS Organizations to define rules for how tags can be used on AWS resources in your accounts
in AWS Organizations. Tag Policies allow you to easily adopt a standardized approach for tagging
