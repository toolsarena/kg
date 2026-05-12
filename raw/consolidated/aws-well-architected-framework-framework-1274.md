---
title: "AWS Well-Architected Framework Framework"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 674
---

# AWS Well-Architected Framework Framework

In our two previous examples, we include the steady state metrics of less than 0.01% increase
in server-side (5xx) errors and less than one minute of database read and write errors.
The 5xx errors are a good metric because they are a consequence of the failure mode that
a client of the workload will experience directly. The database errors measurement is good
as a direct consequence of the fault, but should also be supplemented with a client impact
measurement such as failed customer requests or errors surfaced to the client. Additionally,
include a synthetic monitor (also known as a user canary) on any APIs or URIs directly
accessed by the client of your workload.
e. Improve the workload design for resilience.
If steady state was not maintained, then investigate how the workload design can be
improved to mitigate the fault, applying the best practices of the AWS Well-Architected
Reliability pillar. Additional guidance and resources can be found in the AWS Builder’s Library,
which hosts articles about how to improve your health checks or employ retries with backoff
in your application code, among others.
After these changes have been implemented, run the experiment again (shown by the dotted
line in the chaos engineering flywheel) to determine their effectiveness. If the verify step
indicates the hypothesis holds true, then the workload will be in steady state, and the cycle
continues.
4. Run experiments regularly.
A chaos experiment is a cycle, and experiments should be run regularly as part of chaos
engineering. After a workload meets the experiment’s hypothesis, the experiment should be
automated to run continually as a regression part of your CI/CD pipeline. To learn how to do
this, see this blog on how to run AWS FIS experiments using AWS CodePipeline. This lab on
recurrent AWS FIS experiments in a CI/CD pipeline allows you to work hands-on.
Fault injection experiments are also a part of game days (see REL12-BP05 Conduct game
days regularly). Game days simulate a failure or event to verify systems, processes, and team
responses. The purpose is to actually perform the actions the team would perform as if an
exceptional event happened.
5. Capture and store experiment results.
Results for fault injection experiments must be captured and persisted. Include all necessary
data (such as time, workload, and conditions) to be able to later analyze experiment results and


# AWS Well-Architected Framework Framework

trends. Examples of results might include screenshots of dashboards, CSV dumps from your
metric’s database, or a hand-typed record of events and observations from the experiment.
Experiment logging with AWS FIS can be part of this data capture.

# AWS Well-Architected Framework Framework

• Litmus