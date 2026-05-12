from store.sparql_store import SPARQLStore
from llm.provider import LLMProvider
from agent.prompts import SPARQL_SYSTEM, SPARQL_GEN_PROMPT


class SPARQLAgent:
    def __init__(self, store: SPARQLStore, llm: LLMProvider):
        self.store = store
        self.llm = llm

    def generate_sparql(self, question: str) -> str:
        schema_hint = self._get_schema_hint()
        prompt = SPARQL_GEN_PROMPT.format(question=question, schema_hint=schema_hint)
        raw = self.llm.generate(prompt, system=SPARQL_SYSTEM)
        # clean up
        raw = raw.strip()
        if raw.startswith("```"):
            raw = raw.split("\n", 1)[1] if "\n" in raw else raw[3:]
            if raw.endswith("```"):
                raw = raw[:-3]
        return raw.strip()

    def execute(self, question: str) -> dict:
        sparql = self.generate_sparql(question)
        print(f"  -> Generated SPARQL:\n{sparql}\n")
        try:
            results = self.store.query(sparql)
            return {"sparql": sparql, "results": results, "error": None}
        except Exception as e:
            # retry once with error context
            retry_prompt = (
                f"The SPARQL query failed with error: {e}\n"
                f"Original query:\n{sparql}\n\n"
                f"Fix the query. Return ONLY valid SPARQL."
            )
            fixed = self.llm.generate(retry_prompt, system=SPARQL_SYSTEM).strip()
            if fixed.startswith("```"):
                fixed = fixed.split("\n", 1)[1] if "\n" in fixed else fixed[3:]
                if fixed.endswith("```"):
                    fixed = fixed[:-3]
            fixed = fixed.strip()
            print(f"  -> Retry SPARQL:\n{fixed}\n")
            try:
                results = self.store.query(fixed)
                return {"sparql": fixed, "results": results, "error": None}
            except Exception as e2:
                return {"sparql": fixed, "results": [], "error": str(e2)}

    def _get_schema_hint(self) -> str:
        types = self.store.get_all_types()
        if types:
            return f"Available types in the graph: {', '.join(types)}"
        return ""
