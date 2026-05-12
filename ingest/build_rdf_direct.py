"""
Generate RDF from Well-Architected Framework markdown files.
Parses text patterns to extract AWS services, concepts, relationships.
No LLM needed — pure text extraction.
"""
import os
import re
from pathlib import Path
from slugify import slugify
from rdflib import Graph, Namespace, Literal, RDF, RDFS
from rdflib.namespace import SKOS, DCTERMS

KG = Namespace("http://kg.local/ontology#")
KGR = Namespace("http://kg.local/resource/")

# Known AWS services for matching
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
]

# Well-Architected pillars and concepts
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
]


def make_id(name):
    return re.sub(r'[^a-z0-9_]', '_', name.lower().strip()).strip('_')[:80]


def extract_from_file(filepath, g):
    text = filepath.read_text(encoding="utf-8", errors="ignore")

    # extract title from frontmatter
    title_match = re.search(r'title:\s*"([^"]+)"', text)
    title = title_match.group(1) if title_match else filepath.stem
    page_id = make_id(title)

    # add document node
    doc_uri = KGR[f"doc_{page_id}"]
    g.add((doc_uri, RDF.type, KG.Document))
    g.add((doc_uri, SKOS.prefLabel, Literal(title)))
    g.add((doc_uri, DCTERMS.source, Literal(filepath.name)))

    body = text.lower()
    found_services = set()
    found_concepts = set()
    found_pillars = set()

    # find AWS services mentioned
    for svc in AWS_SERVICES:
        if svc.lower() in body:
            svc_id = make_id(svc)
            found_services.add((svc_id, svc))

    # find pillars mentioned
    for pillar in WA_PILLARS:
        if pillar.lower() in body:
            p_id = make_id(pillar)
            found_pillars.add((p_id, pillar))

    # find concepts mentioned
    for concept in WA_CONCEPTS:
        if concept.lower() in body:
            c_id = make_id(concept)
            found_concepts.add((c_id, concept))

    # add nodes and edges
    for svc_id, svc_name in found_services:
        svc_uri = KGR[svc_id]
        g.add((svc_uri, RDF.type, KG.Service))
        g.add((svc_uri, SKOS.prefLabel, Literal(svc_name)))
        g.add((doc_uri, DCTERMS.references, svc_uri))

    for p_id, p_name in found_pillars:
        p_uri = KGR[p_id]
        g.add((p_uri, RDF.type, KG.Concept))
        g.add((p_uri, SKOS.prefLabel, Literal(p_name)))
        g.add((p_uri, RDFS.comment, Literal("Well-Architected Pillar")))
        g.add((doc_uri, SKOS.broader, p_uri))

    for c_id, c_name in found_concepts:
        c_uri = KGR[c_id]
        g.add((c_uri, RDF.type, KG.Concept))
        g.add((c_uri, SKOS.prefLabel, Literal(c_name)))
        g.add((doc_uri, SKOS.related, c_uri))

    # service-to-pillar relationships (if both mentioned in same doc)
    for svc_id, svc_name in found_services:
        for p_id, p_name in found_pillars:
            g.add((KGR[svc_id], KG.relates_to, KGR[p_id]))

    # service-to-concept relationships
    for svc_id, svc_name in found_services:
        for c_id, c_name in found_concepts:
            g.add((KGR[svc_id], KG.relates_to, KGR[c_id]))

    # concept-to-pillar relationships
    for c_id, c_name in found_concepts:
        for p_id, p_name in found_pillars:
            g.add((KGR[c_id], SKOS.broader, KGR[p_id]))

    return len(found_services) + len(found_concepts) + len(found_pillars)


def main():
    raw_dir = Path("raw/consolidated")
    out_path = Path("graphify-out/graph.ttl")

    g = Graph()
    g.bind("kg", KG)
    g.bind("kgr", KGR)
    g.bind("skos", SKOS)
    g.bind("dcterms", DCTERMS)

    # load base ontology
    base = Path("model/templates/base_ontology.ttl")
    if base.exists():
        g.parse(str(base), format="turtle")

    md_files = sorted([Path(raw_dir, f) for f in os.listdir(str(raw_dir)) if f.endswith('.md')])
    print(f"Processing {len(md_files)} files...")

    total_entities = 0
    for i, f in enumerate(md_files):
        if i % 200 == 0:
            print(f"  [{i}/{len(md_files)}] {len(g)} triples so far...")
        total_entities += extract_from_file(f, g)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    g.serialize(str(out_path), format="turtle")
    print(f"\nDone!")
    print(f"  Files processed: {len(md_files)}")
    print(f"  Total triples: {len(g)}")
    print(f"  Saved: {out_path}")


if __name__ == "__main__":
    main()
