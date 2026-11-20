import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cards  # noqa: E402
import check  # noqa: E402

CONCEPT = """---
id: ana1/limits
title: Limits
lecture: 3
prerequisites: [ana1/sequences]
exam_weight: 3   # high
sources: ["L03 slides 12-18"]
status: draft
---

See [sequences](sequences.md).
"""

COURSE = """---
course: ana1
status: active
---

[Map](map.md)
"""


def build(root):
    course = root / "fau/2026-ws/ana1"
    (course / "concepts").mkdir(parents=True)
    (course / "README.md").write_text(COURSE)
    (course / "map.md").write_text("[Limits](concepts/limits.md)\n")
    (course / "concepts/limits.md").write_text(CONCEPT)
    (course / "concepts/sequences.md").write_text(CONCEPT.replace("ana1/limits", "ana1/sequences").replace("(sequences.md)", "(limits.md)"))
    (course / "cards.tsv").write_text("What is a limit?\tThe value the tail stays near\tana1/limits\n")
    return course


class CheckTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.course = build(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def test_valid_course_passes(self):
        self.assertEqual(check.check(self.root), [])

    def test_front_matter_parsing(self):
        meta = check.parse_front_matter(CONCEPT)
        self.assertEqual(meta["prerequisites"], ["ana1/sequences"])
        self.assertEqual(meta["sources"], ["L03 slides 12-18"])
        self.assertEqual(meta["exam_weight"], "3")

    def test_firewall_blocks_private_folders_and_pdfs(self):
        (self.course / "sources").mkdir()
        (self.course / "sources/L01.md").write_text("transcript")
        (self.course / "slides.pdf").write_bytes(b"%PDF")
        problems = "\n".join(check.check(self.root))
        self.assertIn("private-only", problems)
        self.assertIn(".pdf", problems)

    def test_wrong_id_and_missing_keys(self):
        (self.course / "concepts/limits.md").write_text(CONCEPT.replace("id: ana1/limits", "id: ana1/other").replace("status: draft\n", ""))
        problems = "\n".join(check.check(self.root))
        self.assertIn("id should be ana1/limits", problems)
        self.assertIn("missing status", problems)

    def test_broken_link_and_bad_cards(self):
        (self.course / "map.md").write_text("[Gone](concepts/gone.md) [web](https://example.org)\n")
        (self.course / "cards.tsv").write_text("only front\n")
        problems = "\n".join(check.check(self.root))
        self.assertIn("broken link: concepts/gone.md", problems)
        self.assertIn("front<TAB>back<TAB>tags", problems)
        self.assertNotIn("example.org", problems)

    def test_cards_export_tags_course(self):
        rows = cards.collect(self.root)
        self.assertEqual(rows, [("What is a limit?", "The value the tail stays near", "ana1 ana1/limits")])


if __name__ == "__main__":
    unittest.main()
