#!/usr/bin/env python3
"""Check the studies repository before committing.

Checks:
- no forbidden files (PDFs, slide decks, recordings, Office files, archives),
- no private-only folders (sources/, homework/, exam/, grades/) in this public repo,
- concept files have complete, valid front-matter whose id matches their path,
- course READMEs name the right course and a valid status,
- relative Markdown links point at files that exist,
- cards.tsv lines have exactly three tab-separated fields.

Usage: python3 tools/check.py [repo-dir]. Exits 1 if anything is wrong.
"""
import json
import re
import sys
from pathlib import Path

FORBIDDEN_SUFFIXES = {
    ".pdf", ".ppt", ".pptx", ".key", ".odp", ".doc", ".docx", ".odt",
    ".mp4", ".mov", ".mkv", ".webm", ".m4a", ".mp3", ".wav", ".zip", ".7z", ".rar",
}
PRIVATE_DIRS = {"sources", "homework", "exam", "grades", "sessions"}
CONCEPT_KEYS = ("id", "title", "lecture", "prerequisites", "exam_weight", "sources", "status")
CONCEPT_STATUS = {"draft", "checked"}
COURSE_STATUS = {"active", "passed", "failed", "dropped", "planned"}
SKIP_DIRS = {".git", "node_modules", ".obsidian"}
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def parse_front_matter(text):
    """Parse a small YAML subset: `key: value`, `key: [a, b]`, `# comments`."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    data = {}
    for line in text[4:end].splitlines():
        line = re.sub(r"\s+#.*$", "", line).strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = (part.strip() for part in line.split(":", 1))
        if value.startswith("[") and value.endswith("]"):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                inner = value[1:-1].strip()
                value = [item.strip().strip("\"'") for item in inner.split(",")] if inner else []
        else:
            value = value.strip("\"'")
        data[key] = value
    return data


def files(root):
    for path in sorted(root.rglob("*")):
        if path.is_file() and not SKIP_DIRS.intersection(path.relative_to(root).parts):
            yield path


def check(root):
    root = Path(root).resolve()
    problems = []

    def problem(path, message):
        problems.append(f"{path.relative_to(root)}: {message}")

    for path in files(root):
        rel = path.relative_to(root)
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            problem(path, f"{path.suffix} files don't belong in git (course material stays on disk; see AGENTS.md)")
        if rel.parts and rel.parts[0] != "method":
            private = PRIVATE_DIRS.intersection(rel.parts[:-1])
            if private:
                problem(path, f"'{sorted(private)[0]}/' is private-only; it belongs in studies-private")

        in_templates = rel.parts[:2] == ("method", "templates")
        if path.suffix == ".md" and not in_templates:
            text = path.read_text(encoding="utf-8")
            text = re.sub(r"```.*?```", "", text, flags=re.S)  # links in code are examples
            text = re.sub(r"`[^`\n]*`", "", text)
            for target in LINK.findall(text):
                if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                    continue
                target_path = (path.parent / target.split("#", 1)[0]).resolve()
                if not target_path.exists():
                    problem(path, f"broken link: {target}")

        if path.parent.name == "concepts" and path.suffix == ".md" and not in_templates:
            check_concept(path, problem)
        if path.name == "README.md" and len(rel.parts) == 4 and not in_templates:
            check_course_readme(path, problem)
        if path.name == "cards.tsv":
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if line.strip() and len(line.split("\t")) != 3:
                    problem(path, f"line {number}: needs front<TAB>back<TAB>tags")
    return problems


def check_concept(path, problem):
    meta = parse_front_matter(path.read_text(encoding="utf-8"))
    if meta is None:
        problem(path, "missing front-matter (copy method/templates/concept.md)")
        return
    missing = [key for key in CONCEPT_KEYS if key not in meta]
    if missing:
        problem(path, "front-matter is missing " + ", ".join(missing))
    course = path.parent.parent.name
    expected = f"{course}/{path.stem}"
    if meta.get("id") and meta["id"] != expected:
        problem(path, f"id should be {expected}, not {meta['id']}")
    if "exam_weight" in meta and str(meta["exam_weight"]) not in {"1", "2", "3"}:
        problem(path, "exam_weight must be 1, 2 or 3")
    if "status" in meta and meta["status"] not in CONCEPT_STATUS:
        problem(path, "status must be draft or checked")
    for key in ("prerequisites", "sources"):
        if key in meta and not isinstance(meta[key], list):
            problem(path, f"{key} must be a list, like [a, b]")


def check_course_readme(path, problem):
    meta = parse_front_matter(path.read_text(encoding="utf-8"))
    if meta is None:
        problem(path, "course README needs front-matter (copy method/templates/course-README.md)")
        return
    if meta.get("course") != path.parent.name:
        problem(path, f"course should be {path.parent.name}")
    if meta.get("status") not in COURSE_STATUS:
        problem(path, "status must be one of " + ", ".join(sorted(COURSE_STATUS)))


def main(argv):
    root = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    problems = check(root)
    for line in problems:
        print(line)
    print(f"{len(problems)} problem(s)" if problems else "All checks passed.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
