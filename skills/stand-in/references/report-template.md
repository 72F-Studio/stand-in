# Report template

Adapt section depth to the decision. Keep the order: the reader should meet
the warning, then the answer to their decision, then the support.

```markdown
# Synthetic interview report: <product or question>

> **Speculative research.** No real people were interviewed. The
> participants below are simulated, and their answers are limited to public
> online sources gathered on <date>. Those sources over-represent people who
> post and review. Use this to form hypotheses and to decide what to check
> with real people, not as proof of what your audience wants.

## Brief
What is being decided, for whom, and the research questions.

## What this suggests for your decision
Three to five statements, each with its confidence meter and the evidence
entries behind it. Lead with whatever most affects the decision, including
unwelcome news.

## Panel
One card per persona: segment, context, grounding entries, assumed
attributes.

## Themes
For each theme:
- What the evidence suggests, and for which segments
- Confidence, with the weakest link named
- Where segments or sources disagree
- Evidence: [n], [n]

## Riskiest assumptions
The beliefs that would hurt most if wrong, ranked by cost of being wrong
against strength of evidence.

## Verify in person
A checklist of everything this round could not meaningfully find, derived
from the session: No data answers, Low-confidence answers that bear on the
decision, questions about future behaviour, extrapolations, contradictions,
segments that could not be found online, and anything text cannot show.
Most costly to get wrong first. For each item:

- [ ] **The point to verify**
  - Why this round could not settle it
  - Who to ask, and where to find them
  - One to three questions, about past behaviour

## Interview transcripts
Question by question, each answer with its evidence and confidence lines.

## Evidence log
Every numbered entry with its link, date, type, speaker segment and how it
was retrieved.

## Limits
The biases that apply to this particular evidence set.
```

Wording throughout: "the evidence suggests", "sources for this segment
report". Avoid "users said", "participants told us", percentages of the
panel, or anything else that reads as a sampled study.

## HTML report

`assets/report-template.html` renders the same report as a single
self-contained page, with drawn confidence meters, a summary of how many
answers sit at each confidence level, a persona filter on the transcripts,
and citations that jump to the evidence log. It works offline, in light and
dark mode, and prints cleanly.

To fill it, copy the file and replace the JSON in the
`<script id="report-data">` block. Leave everything else untouched,
including the warning banner. Rules for the JSON:

- It must be valid JSON. Inside any string, write `<\/` in place of `</`.
- Every string is shown as plain text; do not put HTML or Markdown in it.
- Remove every `REPLACE:` placeholder. The page shows a red alert while any
  remain.
- Omit a section by giving it an empty list.

| Field | Contents |
| --- | --- |
| `title`, `date` | Product or question; the date the evidence was gathered |
| `brief` | `what`, `who`, `decision`, and a `questions` list |
| `findings[]` | `statement`, `confidence`, `reason`, `evidence` |
| `panel[]` | `id`, `name`, `descriptor`, `segment`, `context`, `grounding`, `assumed` |
| `themes[]` | `title`, `summary`, `confidence`, `reason`, `disagreement`, `evidence` |
| `assumptions[]` | `assumption`, `why`, `confidence` |
| `verifyInPerson[]` | `point`, `why` (why the round could not settle it), `who`, `where`, and a `questions` list; most costly to get wrong first |
| `transcript[]` | `question` and `answers[]`, each with `persona` (a panel `id`), `answer`, `evidenceNote`, `evidence`, `confidence`, `reason` |
| `evidence[]` | `n`, `source`, `url`, `date`, `type`, `speaker`, `signal`, `scale`, `retrieved` |
| `limits[]` | Strings: the biases that apply to this evidence set |

`confidence` is one of `high`, `medium`, `low` or `none`. `evidence` and
`grounding` are lists of evidence numbers, each matching an `n` in the
evidence log. `url` must start with `http://` or `https://`; leave it empty
when there is no link. For a No data answer, put the out-of-character
statement in `answer`, set `confidence` to `none`, and use `reason` for what
would answer the question.
