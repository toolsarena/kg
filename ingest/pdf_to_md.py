import re
import sys
import click
import pdfplumber
from pathlib import Path
from slugify import slugify

MAX_SECTION_CHARS = 12000  # ~3K tokens — fits comfortably in qwen 7b context


def extract_pages(pdf_path: Path) -> list[dict]:
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        total = len(pdf.pages)
        for i, page in enumerate(pdf.pages):
            if i % 50 == 0:
                print(f"  Reading page {i+1}/{total}...", flush=True)
            text = page.extract_text() or ""
            tables = page.extract_tables() or []
            table_md = ""
            for table in tables:
                if table and len(table) > 1:
                    header = "| " + " | ".join(str(c or "") for c in table[0]) + " |"
                    sep = "| " + " | ".join("---" for _ in table[0]) + " |"
                    rows = "\n".join(
                        "| " + " | ".join(str(c or "") for c in row) + " |"
                        for row in table[1:]
                    )
                    table_md += f"\n{header}\n{sep}\n{rows}\n"
            pages.append({"page_num": i + 1, "text": text, "tables": table_md})
    print(f"  Read {total} pages")
    return pages


def is_heading(line: str) -> bool:
    s = line.strip()
    if not s or len(s) > 120 or len(s.split()) > 12:
        return False
    if s.startswith("#"):
        return True
    if s.isupper() and len(s) > 3:
        return True
    if re.match(r"^(\d+\.?\s+)?[A-Z][A-Za-z0-9 :&\-/,()]+$", s) and len(s.split()) <= 10:
        return True
    return False


def split_into_sections(pages: list[dict], pdf_name: str) -> list[dict]:
    sections = []
    current = {"title": "Untitled", "body": "", "page_num": 1}

    for page in pages:
        text = page["text"].strip()
        # strip noise
        text = re.sub(r"^\d+\s*$", "", text, flags=re.MULTILINE)
        text = re.sub(r"Confluence\s+Export", "", text, flags=re.IGNORECASE)
        text = re.sub(r"^\s*(Page \d+ of \d+)\s*$", "", text, flags=re.MULTILINE)

        for line in text.split("\n"):
            if is_heading(line):
                if current["body"].strip():
                    sections.append(current)
                current = {
                    "title": line.strip().lstrip("#").strip(),
                    "body": "",
                    "page_num": page["page_num"],
                }
            else:
                current["body"] += line + "\n"

        if page["tables"]:
            current["body"] += page["tables"]

    if current["body"].strip():
        sections.append(current)

    if not sections:
        all_text = "\n".join(p["text"] for p in pages)
        sections = [{"title": pdf_name, "body": all_text, "page_num": 1}]

    # chunk oversized sections so LLM can handle them
    chunked = []
    for sec in sections:
        if len(sec["body"]) <= MAX_SECTION_CHARS:
            chunked.append(sec)
        else:
            parts = chunk_text(sec["body"], MAX_SECTION_CHARS)
            for j, part in enumerate(parts):
                chunked.append({
                    "title": f"{sec['title']} (Part {j+1})",
                    "body": part,
                    "page_num": sec["page_num"],
                })

    return chunked


def chunk_text(text: str, max_chars: int) -> list[str]:
    """Split text into chunks at paragraph boundaries."""
    paragraphs = re.split(r"\n\s*\n", text)
    chunks, current = [], ""
    for para in paragraphs:
        if len(current) + len(para) > max_chars and current:
            chunks.append(current.strip())
            current = para + "\n\n"
        else:
            current += para + "\n\n"
    if current.strip():
        chunks.append(current.strip())
    return chunks if chunks else [text]


def save_sections(sections: list[dict], pdf_path: Path, out_dir: Path):
    pdf_name = pdf_path.stem
    folder = out_dir / slugify(pdf_name)
    folder.mkdir(parents=True, exist_ok=True)

    for i, section in enumerate(sections):
        slug = slugify(section["title"]) or f"section-{i}"
        # truncate slug to avoid filesystem limits
        slug = slug[:80]
        frontmatter = (
            f"---\n"
            f'title: "{section["title"]}"\n'
            f'source_pdf: "{pdf_path.name}"\n'
            f'pdf_page: {section["page_num"]}\n'
            f"---\n\n"
        )
        content = frontmatter + f"# {section['title']}\n\n{section['body'].strip()}\n"
        out_file = folder / f"{slug}.md"
        counter = 1
        while out_file.exists():
            out_file = folder / f"{slug}-{counter}.md"
            counter += 1
        out_file.write_text(content, encoding="utf-8")

    print(f"  -> {len(sections)} sections saved to {folder}")
    return folder


@click.command()
@click.option("--input", "input_path", required=True, help="PDF file or folder of PDFs")
@click.option("--out", "out_dir", default="raw", help="Output directory")
def main(input_path, out_dir):
    input_path = Path(input_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    pdfs = [input_path] if input_path.is_file() else list(input_path.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found at {input_path}")
        return

    for pdf in pdfs:
        print(f"Processing: {pdf.name}")
        pages = extract_pages(pdf)
        sections = split_into_sections(pages, pdf.stem)
        save_sections(sections, pdf, out_dir)

    print(f"\nDone. Markdown files in: {out_dir}")


if __name__ == "__main__":
    main()
