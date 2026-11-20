#!/usr/bin/env python3
"""Collect every course's cards.tsv into one file Anki can import.

Writes cards-export.tsv (ignored by git) in the repository root. In Anki:
File → Import → choose the file; the header lines set the tab separator and
the tags column. Each card is also tagged with its course.

Usage: python3 tools/cards.py [repo-dir]
"""
import sys
from pathlib import Path


def collect(root):
    rows = []
    for path in sorted(Path(root).glob("*/*/*/cards.tsv")):
        course = path.parent.name
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            front, back, tags = line.split("\t")
            tag_list = tags.split()
            if course not in tag_list:
                tag_list.insert(0, course)
            rows.append((front, back, " ".join(tag_list)))
    return rows


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    rows = collect(root)
    out = root / "cards-export.tsv"
    header = "#separator:tab\n#html:true\n#tags column:3\n"
    out.write_text(header + "".join("\t".join(row) + "\n" for row in rows), encoding="utf-8")
    print(f"Wrote {len(rows)} cards to {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
