# The learning method

How this system tries to get the most learning out of every hour. Each rule says what it is, why it works, and how the agents apply it.

## 1. Test yourself instead of rereading

**Why:** pulling an answer out of memory strengthens it far more than reading it again ("retrieval practice"). Rereading feels productive but mostly builds familiarity.
**Here:** every concept ends with recall questions, and the cards and quizzes come before any rereading. Answers stay hidden until you've tried.

## 2. Spread reviews out

**Why:** memories fade on a curve. A review just as you're about to forget resets the curve and makes it flatter each time ("spaced repetition").
**Here:** `studies-private/tools/due.py` schedules each concept with the SM-2 algorithm (used by Anki's classic scheduler). The interval grows after good answers (1 day, then 6 days, then about ×2.5 each time) and drops back to tomorrow after a miss.

## 3. Grade honestly, 0–5

| Score | Meaning |
| --- | --- |
| 5 | Correct, instantly |
| 4 | Correct after a short think |
| 3 | Correct, but it took real effort |
| 2 | Wrong, but the answer looked familiar |
| 1 | Wrong, only vaguely familiar |
| 0 | Blank |

Scores below 3 count as a miss: the concept comes back tomorrow, and the mistake goes in `mistakes.md`.

## 4. Mix topics

**Why:** practising one type of problem at a time feels smooth, but on the exam you first have to recognise *which* method a problem needs. Mixing builds that skill ("interleaving").
**Here:** practice sets combine concepts from different lectures once a course has more than a few.

## 5. Explain it simply

**Why:** if you can't explain something in plain words, you've found the gap (the Feynman technique).
**Here:** every concept file starts with "In one sentence" and "Intuition". In quizzes, the agent sometimes asks you to explain instead of recall.

## 6. Worked examples first, then do it yourself

**Why:** for new procedures, studying a solved example teaches faster than struggling alone. Once you know the steps, solving it yourself teaches more.
**Here:** each concept has one worked example. The practice problems hide their solutions in `<details>`.

## 7. Let the exam decide what matters

**Why:** time is limited. Past exams show which topics carry the points.
**Here:**
- `exam/blueprint.md` (private) counts topics across past exams. That gives each concept an exam weight from 1 to 3.
- The "what's due" list sorts by due date, then by exam weight.
- Exam mode plans by exam weight × weakness.

## 8. Keep an error log

**Why:** mistakes repeat. Writing down why something went wrong, and what the right idea is, stops the second occurrence.
**Here:** `mistakes.md` (private): date, concept, what I did, why it was wrong, the fix. Practice sets revisit logged mistakes.

## 9. Build something

**Why:** using knowledge in a real project links it to everything else you know, and it's the part you'll still remember in a year.
**Here:** at least one project per course in `project/`. The best ones use your own data or tools, for example statistics on your own Fitbit data, or a feature for nixcare.

## A study session (about 45 minutes)

1. **5 min:** "What's due?" Answer the due cards first.
2. **25 min:** a new concept or practice set, weighted by exam weight.
3. **10 min:** a mixed set of older concepts.
4. **5 min:** the agent records scores and mistakes, and says what's next.

Short daily sessions beat long ones before the exam.
