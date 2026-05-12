from store.sparql_store import SPARQLStore
from llm.provider import LLMProvider
from agent.sparql_agent import SPARQLAgent
from agent.prompts import QA_SYSTEM, QA_PROMPT, DECIDE_PROMPT


class QAEngine:
    def __init__(self, store: SPARQLStore, llm: LLMProvider):
        self.store = store
        self.llm = llm
        self.sparql_agent = SPARQLAgent(store, llm)

    def ask(self, question: str) -> str:
        mode = self._decide_mode(question)
        print(f"  -> Mode: {'SPARQL' if mode == 'A' else 'DIRECT'}")

        if mode == "A":
            return self._sparql_answer(question)
        return self._direct_answer(question)

    def _decide_mode(self, question: str) -> str:
        types = self.store.get_all_types()
        prompt = DECIDE_PROMPT.format(
            question=question,
            node_count=self.store.count(),
            edge_count=self.store.count(),  # approximate
            types=", ".join(t.split("#")[-1].split("/")[-1] for t in types[:10]),
        )
        result = self.llm.generate(prompt).strip().upper()
        return "A" if "A" in result else "B"

    def _sparql_answer(self, question: str) -> str:
        result = self.sparql_agent.execute(question)
        if result["error"]:
            return f"SPARQL failed: {result['error']}\nQuery was:\n{result['sparql']}"

        if not result["results"]:
            # fallback to direct
            return self._direct_answer(question)

        # format results as context and let LLM answer
        context = f"SPARQL query: {result['sparql']}\n\nResults:\n"
        for row in result["results"][:20]:
            context += "  " + " | ".join(f"{k}: {v}" for k, v in row.items()) + "\n"

        prompt = QA_PROMPT.format(question=question, context=context)
        return self.llm.generate(prompt, system=QA_SYSTEM)

    def _direct_answer(self, question: str) -> str:
        # broad SPARQL to get relevant triples
        broad_q = """
        SELECT ?s ?sLabel ?p ?o ?oLabel WHERE {
            ?s ?p ?o .
            OPTIONAL { ?s <http://www.w3.org/2004/02/skos/core#prefLabel> ?sLabel }
            OPTIONAL { ?o <http://www.w3.org/2004/02/skos/core#prefLabel> ?oLabel }
        } LIMIT 100
        """
        try:
            rows = self.store.query(broad_q)
            context = "\n".join(
                f"{r.get('sLabel', r['s'])} --[{r['p'].split('#')[-1].split('/')[-1]}]--> {r.get('oLabel', r['o'])}"
                for r in rows
            )
        except Exception:
            context = "(Could not retrieve graph context)"

        prompt = QA_PROMPT.format(question=question, context=context)
        return self.llm.generate(prompt, system=QA_SYSTEM)
