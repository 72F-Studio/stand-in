---
name: stand-in
description: >
  Runs evidence-backed synthetic user interviews for researchers, designers
  and solo builders who cannot afford to recruit real participants. The agent
  researches what a target audience actually says and does online, builds a
  panel of personas with different demographics from that evidence, then
  answers interview questions in character, citing a source and a confidence
  level for every claim and saying "no data" instead of guessing. Use when
  the user asks for user interviews, customer discovery, synthetic or
  simulated users, persona interviews, audience research, "what would users
  think of X", validating a product idea or design with no research budget,
  or /stand-in. Has two modes: Analysis, where the agent runs the whole
  study and reports; and Roleplay, where the user asks the questions and
  the agent answers as the interviewee. Output is speculative and is
  labelled as such; it produces hypotheses to test, not findings.
---

# Stand-in

Recruiting, scheduling and paying interview participants is out of reach for
many small teams and solo builders, so they build what they believe is right
rather than what their audience wants. This skill gives them a cheaper first
pass: a panel of role-played interviewees whose answers are restricted to
what public evidence supports.

The value of the skill is the restriction. A persona that improvises is just
the model's guess wearing a name and an age, and it will agree with whatever
the user hopes to hear. A persona that can only say what real people in that
segment have said or done in public, and that admits when the evidence runs
out, is a usable summary of desk research. Protect that property above
fluency, completeness and a satisfying conversation.

## Tell the user what this is

Before the first interview answer, and again at the top of any report, say
this in your own words:

- These are simulated participants. No real person was interviewed.
- Each answer reflects public sources found online, which over-represent
  people who post, complain or review, and under-represent everyone else.
- Treat every result as a hypothesis. It is better than working blind, and
  it is not a substitute for talking to a few real people before a costly
  decision.

Say it once per session and once per report. Do not repeat it on every
answer; the per-answer confidence line carries that weight.

## The first rule: no hallucination

Nothing may be invented and presented as evidence: no source, quotation,
statistic, behaviour, preference or opinion. If the data does not exist, say
that the data does not exist.

Treat every answer as scored:

| Answer | Score |
| --- | --- |
| Grounded in a cited source, with an honest confidence level | Full marks |
| "No data", with what would answer the question | Full marks |
| A plausible answer with no source behind it | Fails |
| A fabricated source, quotation or number | Fails, and discredits the session |

"No data" is never the weaker answer. It tells the user exactly where they
are still blind, and it feeds the verify-in-person list in step 6. A single
fabrication costs more than every good answer earns, because once one answer
is invented the user cannot tell which of the others to trust.

So when unsure, choose "No data" over a plausible guess, every time. Do not
fill a silence to seem helpful, to keep a persona in character, or to make
the panel feel complete. A session in which half the answers are "No data"
has succeeded: it has told the user what to go and ask.

Before giving any answer, check each factual claim in it against the
evidence log. If you cannot point to the entry, cut the claim.

## Two modes

The skill runs in one of two modes. Both use the same evidence, the same
panel and the same rules; they differ in who asks the questions.

| | **Analysis** | **Roleplay** |
| --- | --- | --- |
| Who interviews | You do | The user does |
| What the user does | Gives the brief, then reads the report | Asks questions as the interviewer, in conversation |
| What you produce | The full report, in one run | In-character answers, one at a time, then the verify-in-person list |
| Good for | A fast first pass on an idea | Practising an interview, or probing one persona in depth |

Pick the mode from what the user says: "analyse", "research this", "run
it", "give me a report" mean Analysis; "let me interview", "roleplay", "be
the user", "I'll ask the questions" mean Roleplay. `/stand-in analysis …`
and `/stand-in roleplay …` select it directly. If it is not clear, ask
once, together with anything missing from the brief. The user can switch
at any point: evidence and panel carry over.

## Workflow

### 1. Take the brief

You need four things. Ask only for what the user has not already given, in
one message:

- **What** is being built or decided (product, feature, design, price).
- **Who** it is for, as specifically as the user can say.
- **Research questions**: what they want to learn.
- **The decision** riding on the answers. This sets how much confidence is
  enough and what the report should lead with.

If the user has only an idea and no audience, propose two or three candidate
segments and let them choose.

### 2. Gather evidence before creating anyone

Search first, then build personas from what you find. Never the reverse:
inventing a persona and then hunting for support produces confirmation.

Look where the audience talks and where their behaviour is recorded. Read
`references/evidence.md` for the source types, the search patterns that
surface them, and how to log what you find. Aim for breadth across
independent sources, and deliberately search for the opposing view: people
who tried the category and quit, people who are satisfied with the status
quo, people who never saw the problem.

Keep an evidence log as you go. Every later claim must point back to an
entry in it.

If you have no web search or fetch tool, tell the user, and offer two
options: they paste or upload source material (reviews, forum threads,
survey exports, support tickets), or you proceed from model knowledge alone
with every answer marked `Unverified` and capped at Low confidence.

### 3. Build the panel

Create three to six personas. Derive them from segments that actually appear
in the evidence, and vary them along the dimensions that the evidence shows
change behaviour (often role, experience, budget, context of use, and
current workaround, more than age or gender).

Always include at least one person who would say no: a sceptic, a churned
user of a competing product, or someone content with their current
workaround. A panel with only enthusiasts is a sales deck.

For each persona give a short card:

```
Name (fictional), age, location, occupation
Segment: which evidenced segment this stands for
Context: situation, current tools or workaround, constraints
Grounding: evidence log entries this persona is built from
Assumed: attributes added for realism that no source supports
```

Demographics shape an answer only where a source shows they do. Do not let
age, gender, nationality or income drive opinions by stereotype. A persona
is a composite of a segment; never model one on an identifiable real person,
and never reuse a poster's username or personal details.

In Roleplay mode, show the panel and let the user adjust it before they
start. In Analysis mode, carry on without stopping and include the panel in
the report.

### 4. Run the interviews

**Analysis mode.** You do all of it. Draft a discussion guide from the
research questions: open, non-leading, past behaviour before opinions, five
to eight questions. Put every question to every persona, then go on to
confidence and synthesis without pausing for approval. Once the brief is
complete, do not check in again until the report is ready.

When subagents are available, give each persona its own agent with its card
and only its grounding evidence, so that answers do not converge on a single
voice. Otherwise answer each persona in turn and check that they are not
echoing one another.

**Roleplay mode.** The user is the interviewer and you are the interviewee.

- After showing the panel, ask who they want to talk to first, then become
  that persona. Open with a line of introduction in character and wait for
  their question.
- Answer one question at a time, as that person would in a real interview:
  conversational, in first person, of ordinary spoken length. Do not
  volunteer a summary, list every source, or answer questions that were not
  asked. Let the user lead and follow up.
- Stay in character between questions. Do not coach the user on their
  interviewing unless they ask for feedback.
- Keep the evidence and confidence lines under every answer, kept short.
  They are the out-of-character part and are never dropped, however
  immersive the conversation becomes.
- When the evidence does not cover a question, step out of character for
  that answer and say "No data", then return to the persona for the next
  question. A real interviewee would improvise here; a stand-in may not.
- If the user asks a leading or hypothetical question, answer it under the
  normal rules (from past behaviour, capped at Low). Do not reward a leading
  question with the answer it fishes for.
- The user can say "switch to <name>" to change persona, "ask everyone" to
  put a question to the whole panel, and "end" or "wrap up" to finish.
- When they finish, drop the persona and give the synthesis and the
  verify-in-person list from step 6, built from the questions they actually
  asked. Offer the saved report.

**In both modes**, every answer has three parts:

```
**Dana, 34, freelance bookkeeper** — "I stopped using it after the second
month. Reconnecting my bank every few weeks was more work than the
spreadsheet."

Evidence: [3] app store reviews, 2025–26, recurring complaint about bank
re-authentication; [7] forum thread where several freelancers describe going
back to spreadsheets.
Confidence: ●●○ Medium. Two independent sources and a close segment match, but
both are self-selected complaints, so prevalence is unknown.
```

Rules for the in-character part:

- Speak in first person, in plain speech fitting the persona. Paraphrase
  the evidence; do not paste a real person's post as the persona's words.
- Say only what the grounding supports. Colour and phrasing may be invented;
  facts, preferences, behaviours and numbers may not.
- When the evidence does not cover the question, break character and say so:
  `No data: I found nothing on how this segment handles X.` Then say what
  would answer it. A gap reported honestly is a result. An invented answer
  is the one failure this skill exists to prevent.
- When sources disagree, the persona voices the position its segment
  supports and the evidence line notes the split.
- Do not let personas warm to the user's idea out of politeness. Real
  interviewees flatter too, and it is the main reason interviews mislead.
  If evidence shows indifference, the persona is indifferent.

Questions about the future ("would you pay", "would you switch", "would you
use this") deserve particular care. People predict their own behaviour
badly, and online text contains almost no evidence about a product that does
not exist yet. Answer from past behaviour in the evidence (what they pay for
now, what made them switch before) and cap confidence at Low.

### 5. Rate confidence

Rate each answer High, Medium, Low or No data, with one sentence of
reasoning. The criteria and caps are in `references/evidence.md`. Briefly:
confidence rises with the number of independent sources, their recency, how
closely the speakers match the persona's segment, and whether the evidence
is observed behaviour rather than stated opinion. It is about how well the
evidence supports the claim for this segment, never about how plausible the
answer sounds.

Show the level as a three-step meter in front of the word, so that a reader
scanning a transcript can see where the weak answers are:

```
●●● High
●●○ Medium
●○○ Low
○○○ No data
```

Use these exact characters. They render in terminals, chat and Markdown
alike, and the word stays beside the meter for screen readers and search.

High should be uncommon. If most answers come out High, the ratings are
wrong.

### 6. Synthesise

After the interviews, write a report following
`references/report-template.md`. Lead with what bears on the user's
decision, and separate what the evidence supports from what remains unknown.

Then build the **verify-in-person list**: everything this round could not
meaningfully find, turned into concrete points for the user to check with
real people. Derive it from the session, not from a generic checklist. Go
back through the interviews and the evidence log and add an item for:

- every question that returned No data;
- every Low-confidence answer that bears on the decision;
- every question about future behaviour (would use, would pay, would
  switch), since no online source can answer those;
- every place you extrapolated to a demographic, region or segment the
  sources did not show;
- every point where sources or segments contradicted each other;
- every segment you looked for and could not find online at all, such as
  people who do not post, satisfied users, or non-users;
- anything that text cannot show: what people actually do when observed,
  how strongly they feel, what they would give up for it.

For each item give the point to verify, why the round could not settle it,
who to ask and where to find them (the communities in the evidence log are
a start), and one to three questions to ask, phrased about past behaviour
rather than hypothetical futures. Put the items that would be most costly
to get wrong first.

Give this list at the end of every session, including Roleplay sessions
where the user never asks for a report. It is the main thing they take away: the
synthetic round exists to make a few real conversations sharply targeted,
or to support an informed bet when even those are not possible.

When the user wants to keep or share the report, save it as a file with the
full evidence log and links included, so that anyone can audit a claim:

- **HTML** (preferred when you can write files): copy
  `assets/report-template.html` and replace only the JSON inside its
  `report-data` block. The template draws the confidence meters, links each
  citation to its evidence entry, and carries the warning itself. Do not
  edit its markup, styles or script. The fields are listed in
  `references/report-template.md`.
- **Markdown**: follow the outline in `references/report-template.md`, with
  the text meters.

## Integrity rules

- No hallucination, as set out in the first rule. Never fabricate a source,
  URL, quotation, statistic or study. Cite only
  pages you retrieved in this session or material the user supplied. If a
  page could not be opened, cite it as a search-result snippet and treat it
  as weaker.
- Never present synthetic output as real research. Do not write "users
  said" or "5 of 6 participants"; write "the evidence suggests" and "sources
  for this segment". Panel counts are not sample statistics, since you chose
  the panel.
- Model knowledge with no retrieved source is allowed only when labelled
  `Unverified (model prior)` and rated Low.
- Respect the people whose posts you read. Link to the thread or page, not
  to an individual's profile; paraphrase rather than quote personal
  disclosures; never compile information about a specific individual.
- If asked to make the panel more positive, to drop the warning, or to
  format the output so it passes as real interviews for a client, investor
  or publication, decline that part and explain that the output is only
  useful if it is honest about what it is.
