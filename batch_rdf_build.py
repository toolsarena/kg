"""
Batch RDF builder — processes markdown files in chunks of 200,
saves .ttl after each batch so progress is never lost.
No LLM needed — pure pattern matching.
"""
import os
import re
import json
from pathlib import Path
from rdflib import Graph, Namespace, Literal, RDF, RDFS
from rdflib.namespace import SKOS, DCTERMS

KG = Namespace("http://kg.local/ontology#")
KGR = Namespace("http://kg.local/resource/")

BATCH_SIZE = 200
RAW_DIR = Path("raw/consolidated")
OUT_TTL = Path("graphify-out/graph.ttl")
PROGRESS_FILE = Path("graphify-out/.batch_progress.json")
BASE_ONTOLOGY = Path("model/templates/base_ontology.ttl")

# --- Known entities for matching ---
AWS_SERVICES = [
    "Amazon CloudWatch", "AWS CloudTrail", "Amazon EventBridge", "AWS Config",
    "AWS Systems Manager", "Amazon S3", "Amazon EC2", "AWS Lambda",
    "Amazon RDS", "Amazon DynamoDB", "Amazon VPC", "AWS IAM",
    "Amazon Route 53", "Amazon CloudFront", "AWS KMS", "Amazon SNS",
    "Amazon SQS", "AWS X-Ray", "Amazon ECS", "Amazon EKS",
    "AWS Fargate", "Amazon API Gateway", "AWS Step Functions",
    "Amazon Kinesis", "AWS Glue", "Amazon Redshift", "Amazon Aurora",
    "AWS WAF", "AWS Shield", "Amazon GuardDuty", "AWS Security Hub",
    "Amazon Inspector", "AWS Trusted Advisor", "AWS Cost Explorer",
    "AWS Budgets", "Amazon ElastiCache", "AWS Auto Scaling",
    "Elastic Load Balancing", "AWS CloudFormation", "AWS CDK",
    "Amazon Cognito", "AWS Secrets Manager", "AWS Certificate Manager",
    "Amazon Macie", "AWS Organizations", "AWS Control Tower",
    "AWS Service Catalog", "Amazon Detective", "AWS Backup",
    "Amazon EBS", "Amazon EFS", "AWS Transit Gateway",
    "AWS Direct Connect", "Amazon SageMaker", "AWS CodePipeline",
    "AWS CodeBuild", "AWS CodeDeploy", "AWS CodeCommit",
    "Amazon Managed Grafana", "Amazon Managed Service for Prometheus",
    "AWS Resilience Hub", "AWS Fault Injection Simulator",
    "AWS Well-Architected Tool", "AWS Health Dashboard",
    "AWS Personal Health Dashboard", "AWS Compute Optimizer",
    "Amazon DevOps Guru", "AWS Proton", "AWS App Runner",
    "Amazon OpenSearch Service", "AWS PrivateLink", "AWS RAM",
    "AWS SSO", "AWS Directory Service", "Amazon Athena",
    "AWS Lake Formation", "Amazon QuickSight", "AWS DataSync",
    "AWS Storage Gateway", "Amazon FSx", "AWS Outposts",
    "AWS Local Zones", "AWS Wavelength", "Amazon Connect",
    "Amazon Lex", "Amazon Polly", "Amazon Rekognition",
    "Amazon Textract", "Amazon Comprehend", "Amazon Translate",
    "Amazon Transcribe", "AWS IoT Core", "AWS IoT Greengrass",
    "Amazon Managed Blockchain", "Amazon QLDB",
    "AWS Managed Services", "AWS Support", "AWS IQ",
    "AWS Marketplace", "Amazon ECR", "AWS Nitro",
    "AWS Graviton", "Amazon Lightsail", "AWS Batch",
    "AWS ParallelCluster", "Amazon MQ", "Amazon MSK",
    "AWS AppSync", "AWS Amplify", "Amazon Location Service",
    "AWS Network Firewall", "AWS Firewall Manager",
    "Amazon Security Lake", "AWS Artifact",
    "AWS CloudWatch Logs", "AWS CloudWatch Metrics",
    "AWS Identity and Access Management", "AWS CloudHSM",
    "Amazon Simple Storage Service", "Amazon Elastic Compute Cloud",
    "Amazon Relational Database Service", "Amazon Simple Queue Service",
    "Amazon Simple Notification Service", "AWS Key Management Service",
]

WA_PILLARS = [
    "Operational Excellence", "Security", "Reliability",
    "Performance Efficiency", "Cost Optimization", "Sustainability",
]

WA_CONCEPTS = [
    "shared responsibility model", "defense in depth", "least privilege",
    "infrastructure as code", "automation", "observability", "monitoring",
    "incident management", "change management", "runbooks", "playbooks",
    "disaster recovery", "backup and restore", "pilot light",
    "warm standby", "multi-site active/active", "fault isolation",
    "graceful degradation", "throttling", "circuit breaker",
    "load balancing", "auto scaling", "caching", "CDN",
    "microservices", "serverless", "containers", "event-driven",
    "loose coupling", "high availability", "fault tolerance",
    "encryption at rest", "encryption in transit", "identity federation",
    "multi-factor authentication", "network segmentation",
    "vulnerability management", "penetration testing",
    "compliance", "governance", "tagging strategy",
    "cost allocation", "right sizing", "spot instances",
    "reserved instances", "savings plans",
    "well-architected review", "trade-off analysis",
    "design principles", "best practices", "anti-patterns",
    "workload", "component", "architecture",
    "resilience", "elasticity", "scalability",
    "data classification", "data lifecycle",
    "continuous improvement", "game days",
    "chaos engineering", "load testing",
    "deployment strategy", "blue/green deployment",
    "canary deployment", "rolling deployment",
    "immutable infrastructure", "configuration management",
    "idempotent", "stateless", "retry", "timeout",
    "queue", "dead letter queue", "backoff",
    "health check", "failover", "replication",
    "multi-az", "multi-region", "availability zone",
    "recovery point objective", "recovery time objective",
    "RPO", "RTO", "SLA", "SLO", "SLI",
    "telemetry", "tracing", "distributed tracing",
    "logging", "alerting", "dashboards", "metrics",
    "key performance indicator", "KPI",
    "root cause analysis", "post-incident analysis",
    "threat model", "security controls", "guardrails",
    "service control policy", "permission boundary",
    "data protection", "key management", "certificate management",
    "network layer", "security group", "NACL",
    "VPN", "transit gateway", "peering",
    "cost modeling", "cost optimization", "resource optimization",
    "sustainability", "carbon footprint",
]

# Pre-compile lowercase lookups
_svc_lower = [(s, s.lower()) for s in AWS_SERVICES]
_pillar_lower = [(p, p.lower()) for p in WA_PILLARS]
_concept_lower = [(c, c.lower()) for c in WA_CONCEPTS]


def make_id(name):
    return re.sub(r'[^a-z0-9_]', '_', name.lower().strip()).strip('_')[:80]


def extract_from_text(filepath, body_lower, title, g):
    page_id = make_id(title)
    doc_uri = KGR[f"doc_{page_id}"]
    g.add((doc_uri, RDF.type, KG.Document))
    g.add((doc_uri, SKOS.prefLabel, Literal(title)))
    g.add((doc_uri, DCTERMS.source, Literal(filepath.name)))

    found_svcs = set()
    found_pillars = set()
    found_concepts = set()

    for svc, svc_l in _svc_lower:
        if svc_l in body_lower:
            found_svcs.add((make_id(svc), svc))

    for p, p_l in _pillar_lower:
        if p_l in body_lower:
            found_pillars.add((make_id(p), p))

    for c, c_l in _concept_lower:
        if c_l in body_lower:
            found_concepts.add((make_id(c), c))

    # Add nodes + doc edges
    for sid, sname in found_svcs:
        uri = KGR[sid]
        g.add((uri, RDF.type, KG.Service))
        g.add((uri, SKOS.prefLabel, Literal(sname)))
        g.add((doc_uri, DCTERMS.references, uri))

    for pid, pname in found_pillars:
        uri = KGR[pid]
        g.add((uri, RDF.type, KG.Concept))
        g.add((uri, SKOS.prefLabel, Literal(pname)))
        g.add((uri, RDFS.comment, Literal("Well-Architected Pillar")))
        g.add((doc_uri, SKOS.broader, uri))

    for cid, cname in found_concepts:
        uri = KGR[cid]
        g.add((uri, RDF.type, KG.Concept))
        g.add((uri, SKOS.prefLabel, Literal(cname)))
        g.add((doc_uri, SKOS.related, uri))

    # Cross-relationships
    for sid, _ in found_svcs:
        for pid, _ in found_pillars:
            g.add((KGR[sid], KG.relates_to, KGR[pid]))
    for sid, _ in found_svcs:
        for cid, _ in found_concepts:
            g.add((KGR[sid], KG.relates_to, KGR[cid]))
    for cid, _ in found_concepts:
        for pid, _ in found_pillars:
            g.add((KGR[cid], SKOS.broader, KGR[pid]))

    return len(found_svcs) + len(found_pillars) + len(found_concepts)


def init_graph():
    g = Graph()
    g.bind("kg", KG)
    g.bind("kgr", KGR)
    g.bind("skos", SKOS)
    g.bind("dcterms", DCTERMS)
    if BASE_ONTOLOGY.exists():
        g.parse(str(BASE_ONTOLOGY), format="turtle")
    return g


def load_progress():
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text())
    return {"processed": 0, "total_entities": 0}


def save_progress(processed, total_entities):
    PROGRESS_FILE.write_text(json.dumps({
        "processed": processed,
        "total_entities": total_entities,
    }))


def main():
    all_files = sorted([f for f in RAW_DIR.iterdir() if f.suffix == ".md"])
    total = len(all_files)
    print(f"Total markdown files: {total}")

    progress = load_progress()
    start_idx = progress["processed"]
    total_entities = progress["total_entities"]

    if start_idx > 0:
        print(f"Resuming from file {start_idx} ({start_idx}/{total} done)")

    # Load existing TTL if resuming, otherwise start fresh
    g = init_graph()
    if start_idx > 0 and OUT_TTL.exists():
        g.parse(str(OUT_TTL), format="turtle")
        print(f"  Loaded existing TTL: {len(g)} triples")

    batch_num = 0
    for i in range(start_idx, total, BATCH_SIZE):
        batch = all_files[i:i + BATCH_SIZE]
        batch_num += 1
        batch_entities = 0

        for j, filepath in enumerate(batch):
            try:
                text = filepath.read_text(encoding="utf-8", errors="ignore")
                title_match = re.search(r'title:\s*"([^"]+)"', text)
                title = title_match.group(1) if title_match else filepath.stem
                body_lower = text.lower()
                batch_entities += extract_from_text(filepath, body_lower, title, g)
            except Exception as e:
                print(f"  WARN: {filepath.name}: {e}")

        total_entities += batch_entities
        processed = min(i + BATCH_SIZE, total)

        # Save after each batch
        OUT_TTL.parent.mkdir(parents=True, exist_ok=True)
        g.serialize(str(OUT_TTL), format="turtle")
        save_progress(processed, total_entities)

        print(f"  Batch {batch_num}: files {i+1}-{processed}/{total} | "
              f"+{batch_entities} entities | {len(g)} triples total | saved ✓")

    print(f"\nDone! {total} files → {len(g)} triples → {OUT_TTL}")


if __name__ == "__main__":
    main()
