"""
Graph exploration engine — multi-hop drill-down, pivoting, path finding.
Works on graphify's graph.json. Graphistry-inspired but CPU-based.
GPU layout (UMAP, Graphistry) comes later with Bedrock + GPU access.
"""
import json
import networkx as nx
from pathlib import Path
from collections import defaultdict


class GraphExplorer:
    def __init__(self, graph_json_path: Path):
        data = json.loads(graph_json_path.read_text(encoding="utf-8"))
        self.G = nx.DiGraph()
        for n in data.get("nodes", []):
            nid = n.get("id", n.get("name", ""))
            self.G.add_node(nid, **{k: v for k, v in n.items() if k not in ("id", "name")})
        for e in data.get("edges", []):
            src = e.get("source", e.get("from", ""))
            tgt = e.get("target", e.get("to", ""))
            self.G.add_edge(src, tgt, **{k: v for k, v in e.items() if k not in ("source", "target", "from", "to")})

    # --- Drill-down ---
    def expand(self, node_id: str, hops: int = 1, direction: str = "both") -> dict:
        """Multi-hop expansion from a node. Returns subgraph."""
        visited = {node_id}
        frontier = [node_id]
        edges = []

        for _ in range(hops):
            next_frontier = []
            for nid in frontier:
                if direction in ("out", "both"):
                    for _, tgt in self.G.out_edges(nid):
                        edges.append((nid, tgt, self.G.edges[nid, tgt]))
                        if tgt not in visited:
                            visited.add(tgt)
                            next_frontier.append(tgt)
                if direction in ("in", "both"):
                    for src, _ in self.G.in_edges(nid):
                        edges.append((src, nid, self.G.edges[src, nid]))
                        if src not in visited:
                            visited.add(src)
                            next_frontier.append(src)
            frontier = next_frontier

        nodes = {nid: self.G.nodes[nid] for nid in visited}
        return {"nodes": nodes, "edges": edges, "center": node_id, "hops": hops}

    # --- Pivoting ---
    def pivot(self, node_id: str, relation: str = None) -> dict:
        """Pivot from a node — show all connections, optionally filtered by relation type."""
        result = {"incoming": [], "outgoing": []}
        for src, _ in self.G.in_edges(node_id):
            edge = self.G.edges[src, node_id]
            if relation and edge.get("relation") != relation:
                continue
            result["incoming"].append({
                "node": src, "label": self.G.nodes[src].get("label", src),
                "relation": edge.get("relation", ""), **edge
            })
        for _, tgt in self.G.out_edges(node_id):
            edge = self.G.edges[node_id, tgt]
            if relation and edge.get("relation") != relation:
                continue
            result["outgoing"].append({
                "node": tgt, "label": self.G.nodes[tgt].get("label", tgt),
                "relation": edge.get("relation", ""), **edge
            })
        return result

    # --- Path finding ---
    def shortest_path(self, source: str, target: str) -> list[str]:
        try:
            return nx.shortest_path(self.G, source, target)
        except nx.NetworkXNoPath:
            # try undirected
            try:
                return nx.shortest_path(self.G.to_undirected(), source, target)
            except nx.NetworkXNoPath:
                return []

    def all_paths(self, source: str, target: str, max_depth: int = 5) -> list[list[str]]:
        try:
            return list(nx.all_simple_paths(self.G, source, target, cutoff=max_depth))
        except nx.NetworkXError:
            return []

    # --- God nodes ---
    def god_nodes(self, top_n: int = 10) -> list[dict]:
        """Highest-degree nodes — the things everything depends on."""
        degrees = sorted(self.G.degree(), key=lambda x: x[1], reverse=True)[:top_n]
        return [
            {"id": nid, "label": self.G.nodes[nid].get("label", nid),
             "degree": deg, "type": self.G.nodes[nid].get("type", "")}
            for nid, deg in degrees
        ]

    # --- Surprising connections ---
    def cross_community_edges(self) -> list[dict]:
        """Edges that cross community boundaries — often the most interesting."""
        results = []
        for u, v in self.G.edges:
            cu = self.G.nodes[u].get("community")
            cv = self.G.nodes[v].get("community")
            if cu is not None and cv is not None and cu != cv:
                results.append({
                    "source": u, "source_label": self.G.nodes[u].get("label", u),
                    "target": v, "target_label": self.G.nodes[v].get("label", v),
                    "relation": self.G.edges[u, v].get("relation", ""),
                    "source_community": self.G.nodes[u].get("community_name", ""),
                    "target_community": self.G.nodes[v].get("community_name", ""),
                })
        return results

    # --- Filtering ---
    def filter_nodes(self, node_type: str = None, community: int = None,
                     label_contains: str = None) -> list[dict]:
        results = []
        for nid in self.G.nodes:
            attrs = self.G.nodes[nid]
            if node_type and attrs.get("type") != node_type:
                continue
            if community is not None and attrs.get("community") != community:
                continue
            if label_contains and label_contains.lower() not in attrs.get("label", "").lower():
                continue
            results.append({"id": nid, **attrs})
        return results

    # --- Stats ---
    def stats(self) -> dict:
        types = defaultdict(int)
        communities = defaultdict(int)
        relations = defaultdict(int)
        for nid in self.G.nodes:
            types[self.G.nodes[nid].get("type", "unknown")] += 1
            c = self.G.nodes[nid].get("community_name", "unknown")
            communities[c] += 1
        for u, v in self.G.edges:
            relations[self.G.edges[u, v].get("relation", "unknown")] += 1
        return {
            "nodes": self.G.number_of_nodes(),
            "edges": self.G.number_of_edges(),
            "types": dict(types),
            "communities": dict(communities),
            "relations": dict(relations),
        }

    # --- Subgraph export ---
    def subgraph_json(self, node_ids: set) -> dict:
        nodes = [{"id": n, **self.G.nodes[n]} for n in node_ids if n in self.G.nodes]
        edges = [
            {"source": u, "target": v, **self.G.edges[u, v]}
            for u, v in self.G.edges if u in node_ids and v in node_ids
        ]
        return {"nodes": nodes, "edges": edges}

    # --- Fuzzy search ---
    def search(self, query: str, limit: int = 20) -> list[dict]:
        q = query.lower()
        scored = []
        for nid in self.G.nodes:
            attrs = self.G.nodes[nid]
            label = attrs.get("label", nid).lower()
            desc = attrs.get("description", "").lower()
            score = 0
            if q == label:
                score = 100
            elif q in label:
                score = 80
            elif q in nid.lower():
                score = 60
            elif q in desc:
                score = 40
            if score > 0:
                scored.append({"id": nid, "score": score, **attrs})
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:limit]
