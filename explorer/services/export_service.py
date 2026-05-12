"""Export Service — multi-format export and Neptune push with batching."""
import requests
from rdflib import Graph as RDFGraph

from explorer.services.models import PushResult


def export_graph(graph: RDFGraph, format: str) -> bytes:
    """Export an RDF graph in the specified format.

    Args:
        graph: The RDF graph to export.
        format: One of "turtle", "nt" (N-Triples), or "json-ld".

    Returns:
        Serialized graph as bytes.
    """
    format_map = {
        "turtle": "turtle",
        "ttl": "turtle",
        "nt": "nt",
        "n-triples": "nt",
        "ntriples": "nt",
        "json-ld": "json-ld",
        "jsonld": "json-ld",
    }

    rdflib_format = format_map.get(format.lower())
    if not rdflib_format:
        raise ValueError(f"Unsupported export format: {format}. Use turtle, nt, or json-ld.")

    serialized = graph.serialize(format=rdflib_format)
    if isinstance(serialized, str):
        return serialized.encode("utf-8")
    return serialized


def create_batches(graph: RDFGraph, batch_size: int = 1000) -> list[list[tuple]]:
    """Split graph triples into batches of at most batch_size.

    Args:
        graph: The RDF graph to batch.
        batch_size: Maximum triples per batch (default 1000).

    Returns:
        List of batches, each batch is a list of (s, p, o) tuples.
    """
    if batch_size <= 0:
        batch_size = 1000
    if batch_size > 1000:
        batch_size = 1000

    all_triples = list(graph)
    batches = []
    for i in range(0, len(all_triples), batch_size):
        batch = all_triples[i:i + batch_size]
        batches.append(batch)

    return batches


def _triple_to_sparql(s, p, o) -> str:
    """Convert an rdflib triple to SPARQL INSERT DATA syntax."""
    return f"{s.n3()} {p.n3()} {o.n3()} ."


def push_to_neptune(
    graph: RDFGraph,
    endpoint: str,
    batch_size: int = 1000,
    start_batch: int = 0,
) -> PushResult:
    """Push triples to a Neptune/SPARQL endpoint using batched INSERT DATA operations.

    Args:
        graph: The RDF graph to push.
        endpoint: The SPARQL update endpoint URL.
        batch_size: Max triples per batch (capped at 1000).
        start_batch: Batch index to start from (for retry).

    Returns:
        PushResult with push statistics.
    """
    batches = create_batches(graph, batch_size)
    total_batches = len(batches)
    total_triples = len(graph)
    triples_pushed = 0
    batches_completed = 0

    if start_batch > 0:
        # Skip already-completed batches
        batches = batches[start_batch:]
        batches_completed = start_batch
        triples_pushed = sum(len(b) for b in create_batches(graph, batch_size)[:start_batch])

    for i, batch in enumerate(batches):
        batch_index = start_batch + i
        try:
            # Build SPARQL INSERT DATA query
            triples_str = "\n  ".join(_triple_to_sparql(s, p, o) for s, p, o in batch)
            sparql_update = f"INSERT DATA {{\n  {triples_str}\n}}"

            response = requests.post(
                endpoint,
                data={"update": sparql_update},
                headers={"Content-Type": "application/x-www-form-urlencoded"},
                timeout=60,
            )

            if response.status_code not in (200, 204):
                return PushResult(
                    success=False,
                    total_triples=total_triples,
                    triples_pushed=triples_pushed,
                    batches_completed=batches_completed,
                    total_batches=total_batches,
                    failed_batch=batch_index,
                    error=f"Batch {batch_index} failed: HTTP {response.status_code}",
                )

            triples_pushed += len(batch)
            batches_completed += 1

        except requests.Timeout:
            return PushResult(
                success=False,
                total_triples=total_triples,
                triples_pushed=triples_pushed,
                batches_completed=batches_completed,
                total_batches=total_batches,
                failed_batch=batch_index,
                error=f"Batch {batch_index} failed: request timed out",
            )
        except requests.ConnectionError:
            return PushResult(
                success=False,
                total_triples=total_triples,
                triples_pushed=triples_pushed,
                batches_completed=batches_completed,
                total_batches=total_batches,
                failed_batch=batch_index,
                error="Neptune endpoint unreachable",
            )
        except Exception as e:
            return PushResult(
                success=False,
                total_triples=total_triples,
                triples_pushed=triples_pushed,
                batches_completed=batches_completed,
                total_batches=total_batches,
                failed_batch=batch_index,
                error=f"Batch {batch_index} failed: {e}",
            )

    return PushResult(
        success=True,
        total_triples=total_triples,
        triples_pushed=triples_pushed,
        batches_completed=batches_completed,
        total_batches=total_batches,
        failed_batch=None,
        error=None,
    )
