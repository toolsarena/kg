---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 285
---

# Implementation steps

How can we perform threat modeling?
There are many different ways to perform threat modeling. Much like programming languages,
there are advantages and disadvantages to each, and you should choose the way that works best
for you. One approach is to start with Shostack’s 4 Question Frame for Threat Modeling, which
poses open-ended questions to provide structure to your threat modeling exercise:
1. What are we working on?
The purpose of this question is to help you understand and agree upon the system you are
building and the details about that system that are relevant to security. Creating a model or
diagram is the most popular way to answer this question, as it helps you to visualize what
you are building, for example, using a data flow diagram. Writing down assumptions and
important details about your system also helps you define what is in scope. This allows everyone
contributing to the threat model to focus on the same thing, and avoid time-consuming detours
into out-of-scope topics (including out of date versions of your system). For example, if you are
building a web application, it is probably not worth your time threat modeling the operating
system trusted boot sequence for browser clients, as you have no ability to affect this with your
design.
2. What can go wrong?


# Implementation steps

1. Subscribe to the various blogs and bulletins with your favorite RSS reader or to the Daily
Features Updates SNS topic.