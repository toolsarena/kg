# qgraphify Knowledge Graph Rules

This project has a pre-built knowledge graph in `graphify-out/GRAPH_REPORT.md`.

All responses in this project must follow these standards:

## Source citation standard

Every response must cite its source on the first line using exactly one of:
- `[Graph] graphify-out/GRAPH_REPORT.md`
- `[Graph + Files] graphify-out/GRAPH_REPORT.md + <filename>`
- `[Files] <filename>, <filename>`

This is the same standard as citing references in documentation — every answer must show where it came from.

## Knowledge graph standard

`graphify-out/GRAPH_REPORT.md` must be read before any source file when answering questions about:
- project structure or architecture
- how a component works
- dependencies between modules
- what a class or function does at a high level

The graph is the authoritative source for architecture questions. Raw files are the authoritative source for implementation details.

## File access standard

`listDirectory` and `fileSearch` must not be used to answer architecture questions. The graph already contains the complete project structure. Using directory listing when the graph exists wastes tokens and produces inferior answers.

## Coding standard

When writing or modifying code, always read `graphify-out/GRAPH_REPORT.md` first to identify which god nodes the change touches and which community it belongs to. This prevents unintended side effects on high-degree nodes.
