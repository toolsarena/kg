---
title: "Data management 738"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 743
---

# Data management 738

| Type | AWS Services | Key characteristics |
| --- | --- | --- |
| Relational database | Amazon Aurora, Amazon
RDS, Amazon Redshift. | Designed to support ACID
(atomicity, consistency,
isolation, durability) transacti
ons, and maintain referenti
al integrity and strong data
consistency. Many tradition
al applications, enterpris
e resource planning (ERP),
customer relationship
management (CRM), and
ecommerce use relational
databases to store their data. |
| Key-value database | Amazon DynamoDB | Optimized for common
access patterns, typically
to store and retrieve large
volumes of data. High-traf
fic web apps, ecommerce
systems, and gaming
applications are typical
use-cases for key-value
databases. |
| Document database | Amazon DocumentDB | Designed to store semi-stru
ctured data as JSON-like
documents. These databases
help developers build and
update applications such
as content management,
catalogs, and user profiles
quickly. |
