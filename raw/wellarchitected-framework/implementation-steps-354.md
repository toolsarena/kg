---
title: "Implementation steps"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 514
---

# Implementation steps

• Teams can hold event storming workshops to quickly identify events, commands, aggregates and
domains in a lightweight sticky note format.
• Once domain entities and functions have been formed in a domain context, you can divide your
domain into services using bounded context, where entities that share similar features and
attributes are grouped together. With the model divided into contexts, a template for how to
boundary microservices emerges.
• For example, the Amazon.com website entities might include package, delivery, schedule,
price, discount, and currency.
• Package, delivery, and schedule are grouped into the shipping context, while price, discount,
and currency are grouped into the pricing context.
