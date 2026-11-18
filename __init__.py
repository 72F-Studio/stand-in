"""Hermes plugin for stand-in."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parent
SKILLS_DIR = ROOT / "skills"
COMMAND = "stand-in"


def _skill_prompt(args: str = "") -> str:
    tail = args.strip()
    suffix = f"\n\nUser arguments: {tail}" if tail else ""
    return (
        "Load and follow the Hermes plugin skill "
        "`stand-in:stand-in`. "
        "Run evidence-backed synthetic user interviews and label the results as speculative."
        f"{suffix}"
    )


def rewrite_gateway_command(event: Any = None, gateway: Any = None, **_: Any) -> dict[str, str] | None:
    text = str(getattr(event, "text", "") or "").strip()
    if not text.startswith("/"):
        return None

    head, _, rest = text[1:].partition(" ")
    if head.replace("_", "-").lower() != COMMAND:
        return None

    checker = getattr(gateway, "_check_slash_access", None)
    source = getattr(event, "source", None)
    if checker is not None and source is not None:
        try:
            if checker(source, COMMAND) is not None:
                return None
        except Exception:
            return None

    return {"action": "rewrite", "text": _skill_prompt(rest)}


def _make_command_handler(ctx: Any) -> Callable[[str], str]:
    def handler(raw_args: str) -> str:
        prompt = _skill_prompt(raw_args or "")
        try:
            if ctx.inject_message(prompt):
                return "Queued `stand-in` for the agent."
        except Exception:
            pass
        return prompt

    return handler


def register(ctx: Any) -> None:
    skill_md = SKILLS_DIR / COMMAND / "SKILL.md"
    if skill_md.exists():
        ctx.register_skill(COMMAND, skill_md)

    ctx.register_hook("pre_gateway_dispatch", rewrite_gateway_command)
    ctx.register_command(
        COMMAND,
        _make_command_handler(ctx),
        description="Interview evidence-backed stand-ins for your target users.",
        args_hint="[product, audience or research question]",
    )
