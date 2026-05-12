---
title: "REL06-BP05 Analyze logs"
source_pdf: "wellarchitected-framework.pdf"
pdf_page: 574
---

# REL06-BP05 Analyze logs

Collect log files and metrics histories and analyze these for broader trends and workload insights.
Amazon CloudWatch Logs Insights supports a simple yet powerful query language that you can use
to analyze log data. Amazon CloudWatch Logs also supports subscriptions that allow data to flow
seamlessly to Amazon S3 where you can use or Amazon Athena to query the data. It also supports
queries on a large array of formats. See Supported SerDes and Data Formats in the Amazon Athena
User Guide for more information. For analysis of huge log file sets, you can run an Amazon EMR
cluster to run petabyte-scale analyses.
There are a number of tools provided by AWS Partners and third parties that allow for aggregation,
processing, storage, and analytics. These tools include New Relic, Splunk, Loggly, Logstash,
CloudHealth, and Nagios. However, outside generation of system and application logs is unique to
each cloud provider, and often unique to each service.
An often-overlooked part of the monitoring process is data management. You need to determine
the retention requirements for monitoring data, and then apply lifecycle policies accordingly.
Amazon S3 supports lifecycle management at the S3 bucket level. This lifecycle management can
be applied differently to different paths in the bucket. Toward the end of the lifecycle, you can
transition data to Amazon Glacier for long-term storage, and then expiration after the end of the
retention period is reached. The S3 Intelligent-Tiering storage class is designed to optimize costs
by automatically moving data to the most cost-effective access tier, without performance impact or
operational overhead.
Level of risk exposed if this best practice is not established: Medium
