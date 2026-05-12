import click
from pathlib import Path
from rdflib import Graph


def import_ttl(ttl_path: Path) -> Graph:
    g = Graph()
    g.parse(str(ttl_path), format="turtle")
    print(f"  -> Loaded {len(g)} triples from {ttl_path.name}")
    return g


def import_folder(folder: Path) -> Graph:
    g = Graph()
    for ttl in folder.glob("*.ttl"):
        g.parse(str(ttl), format="turtle")
        print(f"  -> Loaded {len(g)} triples from {ttl.name}")
    return g


@click.command()
@click.option("--ttl", "ttl_path", required=True, help=".ttl file or folder of .ttl files")
def main(ttl_path):
    p = Path(ttl_path)
    if p.is_file():
        g = import_ttl(p)
    elif p.is_dir():
        g = import_folder(p)
    else:
        print(f"Not found: {p}")
        return
    print(f"Total triples: {len(g)}")


if __name__ == "__main__":
    main()
