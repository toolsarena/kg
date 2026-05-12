---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 959
---

# AWS Well-Architected Framework Framework

• Convert payloads and files into optimized formats required by devices. For example, you
can use Amazon Elastic Transcoder or AWS Elemental MediaConvert to convert large, high
quality digital media files into formats that users can play back on mobile devices, tablets, web
browsers, and connected televisions.
• Perform computationally intense activities server-side (such as image rendering), or use
application streaming to improve the user experience on older devices.
• Segment and paginate output, especially for interactive sessions, to manage payloads and
limit local storage requirements.
• Engage suppliers: Work with device suppliers who use sustainable materials and provide
transparency in their supply chains and environmental certifications.
• Use over-the-air (OTA) updates: Use automated over-the-air (OTA) mechanism to deploy
updates to one or more devices.
• You can use a CI/CD pipeline to update mobile applications.
• You can use AWS IoT Device Management to remotely manage connected devices at scale.
• Use managed device farms: To test new features and updates, use managed device farms with
representative sets of hardware and iterate development to maximize the devices supported. For
more details, see SUS06-BP05 Use managed device farms for testing.
• Continue to monitor and improve: Track the energy usage of devices to identify areas for
improvement. Use new technologies or best practices to enhance environmental impacts of
these devices.
