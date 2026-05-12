from pathlib import Path
from rdflib import Graph


class SPARQLStore:
    def __init__(self):
        self.graph = Graph()

    def load_ttl(self, path: Path):
        self.graph.parse(str(path), format="turtle")
        print(f"  -> Store loaded: {len(self.graph)} triples from {path}")

    def load_rdf_graph(self, rdf_graph: Graph):
        self.graph += rdf_graph
        print(f"  -> Store loaded: {len(self.graph)} triples")

    def query(self, sparql: str) -> list[dict]:
        results = self.graph.query(sparql)
        rows = []
        for row in results:
            rows.append({str(var): str(row[var]) for var in results.vars})
        return rows

    def query_raw(self, sparql: str):
        return self.graph.query(sparql)

    def count(self) -> int:
        return len(self.graph)

    def describe(self, uri: str) -> list[tuple]:
        q = f"SELECT ?p ?o WHERE {{ <{uri}> ?p ?o }}"
        return [(str(r.p), str(r.o)) for r in self.graph.query(q)]

    def get_all_types(self) -> list[str]:
        q = "SELECT DISTINCT ?type WHERE { ?s a ?type } ORDER BY ?type"
        return [str(r.type) for r in self.graph.query(q)]

    def get_nodes_by_type(self, type_uri: str) -> list[str]:
        q = f"SELECT ?s WHERE {{ ?s a <{type_uri}> }} ORDER BY ?s"
        return [str(r.s) for r in self.graph.query(q)]
