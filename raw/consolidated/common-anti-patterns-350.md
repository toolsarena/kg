---
title: "Common anti-patterns:"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 494
---

# Common anti-patterns:

• Designing a highly available workload without planning out DNS and network connectivity for
high availability.
• Using public internet addresses on individual instances or containers and managing the
connectivity to them with DNS.
• Using IP addresses instead of domain names for locating services.
• Not testing out scenarios where connectivity to your public endpoints is lost.
• Not analyzing network throughput needs and distribution patterns.
• Not testing and planning for scenarios where internet network connectivity to your public
endpoints of your workload might be interrupted.
• Providing content (like web pages, static assets, or media files) to a large geographic area and
not using a content delivery network.
• Not planning for distributed denial of service (DDoS) attacks. DDoS attacks risk shutting out
legitimate traffic and lowering availability for your users.
Benefits of establishing this best practice: Designing for highly available and resilient network
connectivity ensures that your workload is accessible and available to your users.
Level of risk exposed if this best practice is not established: High


# Common anti-patterns:

• You depend on just one network connection, which creates a single point of failure.
• You use only one VPN tunnel or multiple tunnels that end in the same Availability Zone.