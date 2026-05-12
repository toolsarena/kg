---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 948
---

# Common anti-patterns:

• You process the client requests immediately while it is not needed.
• You do not analyze the requirements for client requests.
Benefits of establishing this best practice: Flattening the demand curve reduce the required
provisioned capacity for the workload. Reducing the provisioned capacity means less energy
consumption and less environmental impact.
Level of risk exposed if this best practice is not established: Low


# Common anti-patterns:

• You overprovision the resources in your cloud workload to meet unforeseen spikes in demand.
• Your architecture does not decouple senders and receivers of asynchronous messages by a
messaging component.