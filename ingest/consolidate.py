"""Merge small markdown sections into neighbors to reduce noise."""
import os
import shutil
from pathlib import Path

MIN_BODY_CHARS = 300  # sections smaller than this get merged into previous


def consolidate(raw_dir: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    # read all files sorted by name (preserves page order)
    files = sorted(raw_dir.iterdir())
    sections = []
    for f in files:
        if not f.suffix == ".md":
            continue
        text = f.read_text(encoding="utf-8")
        # split frontmatter from body
        parts = text.split("---", 2)
        if len(parts) >= 3:
            frontmatter = parts[1].strip()
            body = parts[2].strip()
        else:
            frontmatter = ""
            body = text.strip()
        sections.append({"file": f.name, "frontmatter": frontmatter, "body": body, "full": text})

    # merge small sections into previous
    merged = []
    for sec in sections:
        body_len = len(sec["body"])
        if body_len < MIN_BODY_CHARS and merged:
            # append to previous section
            merged[-1]["body"] += "\n\n" + sec["body"]
            merged[-1]["full"] += "\n\n" + sec["body"]
        else:
            merged.append(dict(sec))

    # write out
    for i, sec in enumerate(merged):
        out_file = out_dir / sec["file"]
        counter = 1
        while out_file.exists():
            stem = sec["file"].rsplit(".", 1)[0]
            out_file = out_dir / f"{stem}-{counter}.md"
            counter += 1
        out_file.write_text(sec["full"], encoding="utf-8")

    print(f"Consolidated: {len(sections)} -> {len(merged)} sections")
    print(f"Output: {out_dir}")
    return len(merged)


if __name__ == "__main__":
    import sys
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("raw/wellarchitected-framework")
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("raw/consolidated")
    consolidate(src, dst)
