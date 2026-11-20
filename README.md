# studies

My university courses, turned into something I can actually learn from. AI agents and I build it together, one lecture at a time.

Every course gets three models:

- **What the course contains:** a map of small concepts, each with the concepts it builds on.
- **What I know:** how sure I am of each concept, and when I last reviewed it.
- **What the exam tests:** how much each topic is worth, from past exams.

From those three, the agents always do the next most useful thing: explain what's new, quiz me on what I'm forgetting, and drill what the exam weighs most.

## Two repositories

| Repository | Visible | Holds |
| --- | --- | --- |
| **studies** (this one) | public | Everything written in my own words: concept explanations, self-made practice problems, flashcards, cheat sheets, one project per course |
| `studies-private` | private | Lecture transcripts, slide and script text, past-exam analysis, graded homework, grades, and my learning progress |

The split protects copyright and exam rules: lecturers' material and graded work never leave the private repository.

## How a course grows

1. **Ingest:** a new lecture's transcript and slide text go into `studies-private`.
2. **Map:** its new concepts are added to the course's `map.md`.
3. **Explain:** each concept gets one short file: plain words, intuition, an example, common mistakes, and recall questions, citing lecture and slide.
4. **Practice:** exam-style problems with worked solutions.
5. **Review:** an agent quizzes me. The results go into my private progress file, and spaced repetition decides what's due next.
6. **Exam mode (last 3 weeks):** a plan from exam weight × weak spots, mock exams, and a cheat sheet.
7. **Project:** at least one per course, ideally tied to something I'm building anyway.

[`method/LEARNING-METHOD.md`](method/LEARNING-METHOD.md) explains why this works. [`AGENTS.md`](AGENTS.md) is the rulebook every AI follows here.

## Layout

```
fau/<semester>/<course>/
  README.md        course card: name, ECTS, exam date and format, status
  map.md           every concept, in order, with prerequisites and exam weight
  concepts/        one short file per concept
  practice/        exam-style problems with worked solutions
  cards.tsv        flashcards (import into Anki)
  cheatsheet.md    built last, from the map
  project/         the course project
method/            the learning method and the file templates
tools/             checks and exports (run `python3 tools/check.py`)
```

Semesters are named like `2026-ws` (winter) and `2027-ss` (summer). A new university is a new top-level folder next to `fau/`.

## Courses

| Semester | Course | Status | Exam |
| --- | --- | --- | --- |
| | *Filled in during onboarding* | | |

## Using it

- **Study:** open a course's `map.md`, or ask an agent "what's due today?". It reads my private progress and quizzes me.
- **Flashcards:** `python3 tools/cards.py` writes one Anki-importable file with every course's cards.
- **Graph view:** the repository opens as an [Obsidian](https://obsidian.md) vault, if I want to see the concept graph.

## License

The notes are [CC BY 4.0](LICENSE.md). The code in `tools/` is MIT. These are a student's notes, not official course material, so check anything important against the lecture.
