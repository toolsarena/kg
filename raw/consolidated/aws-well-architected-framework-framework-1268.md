---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 668
---

# AWS Well-Architected Framework Framework

AWS Fault Injection Service integrates with AWS resources to allow you to run fault injection
experiments for your workloads.
There are also several third-party options for fault injection experiments. These include open-
source tools such as Chaos Toolkit, Chaos Mesh, and Litmus Chaos, as well as commercial options
like Gremlin. To expand the scope of faults that can be injected on AWS, AWS FIS integrates
with Chaos Mesh and Litmus Chaos, allowing you to coordinate fault injection workflows among
multiple tools. For example, you can run a stress test on a pod’s CPU using Chaos Mesh or Litmus
faults while terminating a randomly selected percentage of cluster nodes using AWS FIS fault
actions.
