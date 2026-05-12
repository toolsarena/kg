"""
Converts graphify's graph.json → RDF/Turtle.
This is the only graph layer we build ourselves — graphify doesn't do RDF.
"""
import json
from pathlib import Path
from rdflib import Graph as RDFGraph, Namespace, Literal, URIRef, RDF, RDFS
from rdflib.namespace import SKOS, DCTERMS, OWL
from llm.provider import load_config

KG = Namespace("http://kg.local/ontology#")
KGR = Namespace("http://kg.local/resource/")

EDGE_MAP = {
    "depends_on": DCTERMS.requires,
    "relates_to": SKOS.related,
    "owned_by": DCTERMS.contributor,
    "rationale_for": DCTERMS.description,
    "uses": KG.depends_on,
    "implements": KG.relates_to,
    "calls": KG.depends_on,
    "part_of": SKOS.broader,
    "imports": KG.depends_on,
    "inherits": SKOS.broader,
}

TYPE_MAP = {
    "concept": KG.Concept,
    "service": KG.Service,
    "decision": KG.Decision,
    "team": KG.Team,
    "process": KG.Concept,
    "technology": KG.Concept,
    "class": KG.Concept,
    "function": KG.Concept,
    "module": KG.Concept,
}


def load_graphify_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def graphify_to_rdf(graph_data: dict, config_path: str = "config.yaml") -> RDFGraph:
    cfg = load_config(config_path)

    rdf = RDFGraph()
    rdf.bind("kg", KG)
    rdf.bind("kgr", KGR)
    rdf.bind("skos", SKOS)
    rdf.bind("dcterms", DCTERMS)

    # load ontologies
    base_ttl = cfg.get("ontology", {}).get("base")
    if base_ttl and Path(base_ttl).exists():
        rdf.parse(str(Path(base_ttl)), format="turtle")
    custom_ttl = cfg.get("ontology", {}).get("custom")
    if custom_ttl and Path(custom_ttl).exists():
        rdf.parse(str(Path(custom_ttl)), format="turtle")

    # nodes
    communities_added = set()
    for node in graph_data.get("nodes", []):
        nid = node.get("id", node.get("name", ""))
        node_uri = KGR[nid]
        ntype = node.get("type", "concept")
        rdf_type = TYPE_MAP.get(ntype, KG.Concept)

        rdf.add((node_uri, RDF.type, rdf_type))
        rdf.add((node_uri, SKOS.prefLabel, Literal(node.get("label", node.get("name", nid)))))
        if node.get("description"):
            rdf.add((node_uri, RDFS.comment, Literal(node["description"])))
        if node.get("source"):
            rdf.add((node_uri, DCTERMS.source, Literal(node["source"])))

        comm = node.get("community")
        if comm is not None:
            comm_uri = KGR[f"community_{comm}"]
            rdf.add((node_uri, KG.member_of, comm_uri))
            if comm not in communities_added:
                rdf.add((comm_uri, RDF.type, KG.Community))
                comm_name = node.get("community_name", f"Community {comm}")
                rdf.add((comm_uri, SKOS.prefLabel, Literal(comm_name)))
                communities_added.add(comm)

    # edges
    for edge in graph_data.get("edges", []):
        src = edge.get("source", edge.get("from", ""))
        tgt = edge.get("target", edge.get("to", ""))
        relation = edge.get("relation", edge.get("label", "relates_to"))
        predicate = EDGE_MAP.get(relation, SKOS.related)
        rdf.add((KGR[src], predicate, KGR[tgt]))

    print(f"  -> RDF: {len(rdf)} triples")
    return rdf


def export(graph_json_path: Path, out_path: Path, config_path: str = "config.yaml"):
    data = load_graphify_json(graph_json_path)
    rdf = graphify_to_rdf(data, config_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    rdf.serialize(str(out_path), format="turtle")
    print(f"  -> Saved: {out_path}")
    return rdf
