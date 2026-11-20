# Onboarding: fill both repositories from Marc's course files

A one-time job for an agent with access to Marc's computer, written for Antigravity, but any agent can follow it. Read [`AGENTS.md`](AGENTS.md) first: the firewall applies to every step.

## 0. Set up

Clone both repositories side by side, if they aren't already:

```
git clone https://github.com/mteyra/studies ~/studies
git clone https://github.com/mteyra/studies-private ~/studies-private
```

Work on a branch named `onboarding` in each, and push at the end.

## 1. Inventory: find everything, change nothing

Search the folders Marc names for course material:
- lecture slides and scripts (PDF, PPTX), exercise sheets, past exams;
- **lecture transcripts** (TXT, MD, SRT, VTT, DOCX), recordings;
- Marc's own notes and homework;
- any grade overview (*Notenspiegel*, Transcript of Records).

Also check whether a course already has its own git repository (e.g. a group project); link it, don't copy it.

Write `~/studies-private/INVENTORY.md` with one table:

| Course (full name) | Proposed slug | Semester | Language | What was found (counts by type) | Folder paths |
| --- | --- | --- | --- | --- | --- |

**Stop here and show Marc the table.** He confirms which courses to include, their slugs and their semesters before anything else happens.

## 2. For each confirmed course

`<sem>` is `2026-ws` or `2027-ss` style; `<c>` is the slug.

### Public: `~/studies/fau/<sem>/<c>/`
- `README.md` from `method/templates/course-README.md`. Fill in name, code, ECTS, lecturer, language, and exam date, format and aids, from the syllabus, the first lecture or the StudOn/Campo pages saved in the files. Leave unknown fields empty; don't guess.
- `map.md` from `method/templates/map.md`, with **one row per concept** across all lectures found, in lecture order. Set `exam_weight` 2 by default, or from the blueprint once step 2's private part exists. Status: `draft`. Link only concepts whose file exists; otherwise write the name without a link.
- `concepts/`: concept files **for the first lecture only**, as an example of the format. The rest are written lecture by lecture later (the loop in `AGENTS.md`).
- `cards.tsv`: cards for those concepts.
- `practice/README.md`: one line saying practice sets go here.
- `project/README.md` from `method/templates/project.md`, with **1–3 project ideas**. They should use the course's content on Marc's own data or tools (agentic-secretary, nixcare, rommelweb, the Fitbit data, his NixOS laptop) and be something he'd actually use.

### Private: `~/studies-private/fau/<sem>/<c>/`
Copy the folder `~/studies-private/templates/course/`, then fill it:
- `sources/`:
  - **Transcripts:** one Markdown file per lecture (`L03-transcript.md`, front-matter: lecture, date, original path).
  - **Slides and scripts:** extract the text (`pdftotext -layout`) into `L03-slides.md`.
  - **Never copy PDFs, decks or recordings.** They stay where they are.
  - `sources/index.md`: every source with its original path on disk.
- `exam/blueprint.md`: date, format, aids, admission requirements. If past exams exist, count which topics appear and how many points they carry. That gives each topic an exam weight (1–3), which goes into the public `map.md` as a number only.
- `progress.csv`: one row per concept in the map, with the review columns left empty.
- `homework/`: Marc's own submitted solutions, as text, only if he wants them kept.

## 3. Grades

If a grade overview exists, fill `~/studies-private/grades/grades.csv`: one row per exam attempt.

## 4. Finish

1. Add every course to the table in `~/studies/README.md`.
2. Run both checks; both must pass:
   ```
   python3 ~/studies/tools/check.py
   python3 ~/studies-private/tools/due.py --check
   ```
3. Commit as Marc, no co-author lines, and push `onboarding` in both repositories. Open a pull request in each.
4. Tell Marc:
   - which courses were added;
   - what was missing (no transcripts, no past exams, unknown exam date);
   - which project idea you'd start with, and why.
