from pathlib import Path
from rdflib import Graph
from llm.provider import get_llm


ONTOLOGY_PROMPT = """You are an ontology engineer. The user wants to model a knowledge graph for the following domain:

DOMAIN: {domain}
DESCRIPTION: {description}

Generate an OWL ontology in Turtle (.ttl) format that includes:
1. Classes for the main entity types in this domain
2. Object properties for relationships between entities
3. Datatype properties for attributes
4. Use prefix kg: <http://kg.local/ontology#>
5. Include rdfs:label and rdfs:comment for each term

Return ONLY valid Turtle syntax. No explanation."""


def build_ontology(domain: str, description: str, config_path: str = "config.yaml") -> str:
    llm = get_llm(config_path)
    prompt = ONTOLOGY_PROMPT.format(domain=domain, description=description)
    ttl_text = llm.generate(prompt, system="You are an expert ontology engineer. Output only valid Turtle RDF.")
    # strip markdown fences
    ttl_text = ttl_text.strip()
    if ttl_text.startswith("```"):
        ttl_text = ttl_text.split("\n", 1)[1] if "\n" in ttl_text else ttl_text[3:]
        if ttl_text.endswith("```"):
            ttl_text = ttl_text[:-3]
    return ttl_text.strip()


def save_ontology(ttl_text: str, out_path: Path) -> Graph:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ttl_text, encoding="utf-8")
    g = Graph()
    g.parse(data=ttl_text, format="turtle")
    print(f"  -> Ontology saved: {out_path} ({len(g)} triples)")
    return g


class SchemaRegistry:
    def __init__(self):
        self.graph = Graph()

    def load(self, path: Path):
        self.graph.parse(str(path), format="turtle")
        print(f"  -> Schema loaded: {path} ({len(self.graph)} triples)")

    def load_base(self, config_path: str = "config.yaml"):
        from llm.provider import load_config
        cfg = load_config(config_path)
        base = cfg.get("ontology", {}).get("base")
        if base and Path(base).exists():
            self.load(Path(base))
        custom = cfg.get("ontology", {}).get("custom")
        if custom and Path(custom).exists():
            self.load(Path(custom))

    def get_classes(self) -> list[str]:
        q = "SELECT ?c WHERE { ?c a owl:Class } ORDER BY ?c"
        return [str(row.c) for row in self.graph.query(q)]

    def get_properties(self) -> list[str]:
        q = "SELECT ?p WHERE { ?p a ?t . FILTER(?t IN (owl:ObjectProperty, owl:DatatypeProperty)) } ORDER BY ?p"
        return [str(row.p) for row in self.graph.query(q)]
