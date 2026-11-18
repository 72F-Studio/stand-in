<p align="center"><img src="assets/logo.svg" width="96" alt="stand-in logo"></p>

# stand-in

Interviewing real people is expensive, slow, and often out of reach for small
teams and solo builders. So they build the product they think is right, not
the one their audience wants.

`stand-in` is an agent skill that gives you a first pass for free. Your AI
agent researches what your audience actually says and does online, builds a
panel of personas with different demographics from that evidence, and lets
you interview them. Every answer cites its sources and carries a confidence
level. When the evidence runs out, the persona says so instead of guessing.

> **This is speculative research.** No real people are interviewed. Online
> sources over-represent people who post, complain and review. Treat the
> output as hypotheses: better than working blind, not a substitute for
> talking to a few real people before a costly decision.

## What an answer looks like

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

## How it works

1. **Brief**: what you are building, for whom, what you want to learn, and
   the decision riding on it.
2. **Evidence first**: the agent searches reviews, forums, social posts,
   surveys and statistics, and deliberately looks for people who quit or do
   not care.
3. **Panel**: three to six personas drawn from segments found in the
   evidence, always including at least one sceptic.
4. **Interview**: ask questions live, or let the agent run a discussion
   guide across the panel.
5. **Report**: what the evidence suggests, what could not be found, the
   riskiest assumptions, and a short script for checking them with three to
   five real people. Saved as Markdown, or as a self-contained HTML page with
   drawn confidence meters and citations linked to the evidence log.

Confidence is High, Medium, Low or No data. Questions about future behaviour
("would you pay for this?") are capped at Low, because online text holds
almost no evidence about a product that does not exist yet.

## Install

The skill needs an agent with web search to gather evidence. Without it, the
skill asks you to supply source material or marks everything as unverified.

**Claude Code**

```
/plugin marketplace add 72F-Studio/stand-in
/plugin install stand-in@stand-in
```

**Other agents**: adapters ship for Codex, Gemini / Antigravity, GitHub
Copilot and Copilot CLI, OpenCode, pi, Hermes, Devin, Cursor, Windsurf,
Cline, Kiro, Swival, OpenClaw, and anything that reads `AGENTS.md`. See
[docs/agent-portability.md](docs/agent-portability.md) for which files each
one uses.

**Manually**: copy `skills/stand-in/` into your agent's skills directory
(for Claude Code, `~/.claude/skills/`).

Then ask for it in plain words ("interview some users about my idea for…")
or run `/stand-in`.

## What it will not do

- Invent a source, quotation or statistic.
- Present its output as real interviews, or as "5 of 6 participants said".
- Model a persona on an identifiable person.
- Drop the warning or make the panel friendlier on request.

## License

Copyright (c) 2026 72F Studio.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License version 3 as published by the Free
Software Foundation. It is distributed without any warranty. See
[LICENSE](LICENSE).
