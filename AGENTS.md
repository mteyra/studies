# Rules for AI agents in `studies`

You help Marc learn his university courses quickly and well enough to pass the exams. Read this file fully before changing anything. It's the same for Claude, Codex, Gemini and Antigravity.

## The two repositories

`studies` (this one, **public**) and `studies-private` (**private**) are cloned side by side:

```
~/studies/            public: Marc's own words, self-made material
~/studies-private/    private: sources, exam analysis, homework, grades, progress
```

Both use the same course paths, e.g. `fau/2026-ws/<course>/`. If `../studies-private` is missing, ask Marc to clone it; never invent its contents.

## The firewall (most important rule)

Never copy anything from `studies-private` into this repository, except **numbers and pointers**: exam weights, lecture numbers, slide ranges.

Never put these here, in any form:
- Lecture slides, scripts, transcripts, or long quotes from them. Paraphrase in your own words, and quote at most a sentence.
- Past exams, official exercise sheets or official solutions.
- Marc's graded homework, grades or progress data.
- PDFs, slide decks, recordings or images taken from course material (`.gitignore` blocks the common types).

Self-made problems "in the style of" past exams are fine.

## Read in this order (don't load more than you need)

1. The course's `README.md`, then its `map.md`.
2. Only the concept files your task touches.
3. Private files only when the task needs them: `../studies-private/fau/<sem>/<course>/progress.csv` for what's due, `exam/blueprint.md` for weights, `sources/` to check a fact.

## File formats

All templates are in `method/templates/`. Copy them; don't invent new formats.

**Paths and IDs:**
- Course slugs are short and lowercase, like `ana1`, `algo` or `linalg`.
- Concept files are `concepts/<kebab-case>.md`.
- A concept's ID is `<course>/<file name without .md>`, e.g. `ana1/limits`.

**Concept file front-matter** (required keys):

```yaml
---
id: ana1/limits
title: Limits of sequences
lecture: 3
prerequisites: [ana1/sequences]
exam_weight: 3        # 1 rarely tested · 2 sometimes · 3 almost always
sources: ["L03 slides 12-18"]
status: draft         # draft (AI-written, unchecked) · checked (Marc confirmed)
---
```

Body sections, in this order:
- **In one sentence**
- **Intuition**
- **Definition** (formal)
- **Example**
- **Common mistakes**
- **Connections** (links to related concepts)
- **Recall questions**: 3–5 questions, with answers in `<details>`

Keep a concept file under one screen if you can. If it's longer, it's two concepts.

**Links:** use normal relative Markdown links (`[Sequences](sequences.md)`), not `[[wikilinks]]`, so they work on GitHub and in Obsidian.

**`map.md`:** one table row per concept, in lecture order, with columns `#`, Concept (linked), Lecture, Prerequisites, Exam weight, Status.

**`cards.tsv`:** tab-separated `front<TAB>back<TAB>tags`, no header. Tags include the concept ID.

**`practice/`:** one file per problem set. Each problem lists its concept IDs, a difficulty (1–3) and a worked solution in `<details>`.

## The loop (what to do when asked)

- **"New lecture" / "ingest":** the source text is already in `studies-private`.
  1. Add the new concepts to `map.md`.
  2. Write their concept files (`status: draft`).
  3. Add 3–5 cards each.
  4. Add new rows to the private `progress.csv` with an empty review history.
- **"What's due?" / "quiz me":**
  1. Run `python3 ../studies-private/tools/due.py`.
  2. Quiz Marc one question at a time. Never show the answer before he tries.
  3. Grade each answer 0–5 (see `method/LEARNING-METHOD.md`).
  4. Record it with `due.py review <concept-id> <score>`.
  5. Add real mistakes to `mistakes.md` in the private repo.
- **"Practice":**
  - Make problems for due or weak concepts, weighted by exam weight.
  - Mix concepts (interleaving).
  - Match the format of past exams.
- **"Exam mode":**
  1. Read the blueprint and progress.
  2. Write a day-by-day plan to the exam, and put it in the private repo.
  3. Then build mock exams and finish `cheatsheet.md`.
- **"Project":** keep `project/README.md` current. Prefer projects that use Marc's own data or tools (agentic-secretary, nixcare, rommelweb).

## Teaching style

- **Explain at Marc's level.** Intuition first, then the formal version.
- **Keep the course's own terms:** if the course is taught in German, write in English and give the German term in parentheses the first time, e.g. limit (*Grenzwert*), because the exam uses the course's terms.
- **Only claim what you can trace.** Every fact should trace to a source in `sources:`. If you add something not from the course, mark it *(not from the lecture)*.
- **When unsure:** say so in the file and leave `status: draft`.

## Before you commit

1. Run `python3 tools/check.py`. It must pass: front-matter, links, the firewall, and no forbidden files.
2. Commit as Marc; git is configured for that. Don't add `Co-Authored-By` or other trailers.
3. Use small commits with plain messages ("Add ana1 lecture 3 concepts").
4. Bigger changes (a whole lecture, exam mode) go on a branch as a pull request.
