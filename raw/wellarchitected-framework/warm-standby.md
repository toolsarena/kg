---
title: "Warm standby"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 690
---

# Warm standby

The warm standby approach involves ensuring that there is a scaled down, but fully functional,
copy of your production environment in another Region. This approach extends the pilot light
concept and decreases the time to recovery because your workload is always-on in another
Region. If the recovery Region is deployed at full capacity, then this is known as hot standby.
