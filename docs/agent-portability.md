# Agent portability

The behaviour lives in one place, `skills/stand-in/`. Every other file is a
thin adapter that either exposes that skill to a host or, for hosts that do
not load skills, carries a short rule pointing at it.

## Supported adapters

| Host | Files |
|------|-------|
| Claude Code | `.claude-plugin/`, `skills/` |
| Codex | `.codex-plugin/plugin.json`, `skills/` |
| Gemini / Antigravity | `gemini-extension.json`, `AGENTS.md`, `commands/`, `skills/` |
| GitHub Copilot | `.github/copilot-instructions.md` |
| GitHub Copilot CLI | `.github/plugin/`, `commands/`, `skills/` |
| OpenCode | `opencode.json`, `.opencode/plugins/`, `.opencode/command/`, `skills/` |
| pi | `pi-extension/`, `skills/` |
| Hermes Agent | `plugin.yaml`, `__init__.py`, `skills/` |
| Devin | `.devin-plugin/plugin.json`, `skills/` |
| Cursor | `.cursor/rules/stand-in.mdc` |
| Windsurf | `.windsurf/rules/stand-in.md` |
| Cline | `.clinerules/stand-in.md` |
| Kiro | `.kiro/steering/stand-in.md` |
| Aider / Zed / VS Code Codex / generic agents | `AGENTS.md` |
| Swival | `.swival/skills/stand-in/`, `AGENTS.md` |
| OpenClaw | `.openclaw/skills/stand-in/` |
| Agent rules marketplace | `.agents/rules/`, `.agents/plugins/marketplace.json` |

## Rule-file hosts

Cursor, Windsurf, Cline, Kiro, Copilot and `AGENTS.md` readers do not load
skills. Their rule file tells the agent to read `skills/stand-in/SKILL.md`
and also carries the essential rules inline, so it still behaves correctly
if only the rule file was copied. For the full behaviour (search patterns,
confidence caps, report template), copy `skills/stand-in/` into the project
alongside the rule file.

## Runtime requirement

The host agent needs web search and page fetching to gather evidence.
Without them the skill asks the user for source material or marks every
answer as unverified.

## Editing

Two files are canonical:

- `skills/stand-in/` for the skill
- `.agents/rules/stand-in.md` for the short rule

After changing either, regenerate the copies:

```bash
./scripts/sync-adapters.sh          # rewrite generated adapters
./scripts/sync-adapters.sh --check  # fail if any are out of date
```
