---
title: "Implementation guidance"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 760
---

# Implementation guidance

A cache is a software or hardware component aimed at storing data so that future requests for the
same data can be served faster or more efficiently. The data stored in a cache can be reconstructed
if lost by repeating an earlier calculation or fetching it from another data store.
Data caching can be one of the most effective strategies to improve your overall application
performance and reduce burden on your underlying primary data sources. Data can be cached
at multiple levels in the application, such as within the application making remote calls, known
as client-side caching, or by using a fast secondary service for storing the data, known as remote
caching.
