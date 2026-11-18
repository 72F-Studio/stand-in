#!/usr/bin/env bash
# Regenerates every per-agent adapter from the two canonical sources:
#   skills/stand-in/           the skill
#   .agents/rules/stand-in.md  the short rule for agents that do not load skills
# Run with --check to fail if a generated file is out of date.
set -euo pipefail
cd "$(dirname "$0")/.."

out=$(mktemp -d)
trap 'rm -rf "$out"' EXIT
rule=.agents/rules/stand-in.md

emit() { mkdir -p "$out/$(dirname "$1")"; cat > "$out/$1"; }

emit AGENTS.md < "$rule"
emit .github/copilot-instructions.md < "$rule"
emit .windsurf/rules/stand-in.md < "$rule"
emit .clinerules/stand-in.md < "$rule"
{
  printf -- '---\ndescription: Run evidence-backed synthetic user interviews with cited sources and confidence levels.\nglobs:\nalwaysApply: false\n---\n\n'
  cat "$rule"
} | emit .cursor/rules/stand-in.mdc
{
  printf -- '---\ntitle: Stand-in synthetic user interviews\ninclusion: manual\n---\n\n'
  cat "$rule"
} | emit .kiro/steering/stand-in.md

for host in .swival .openclaw; do
  mkdir -p "$out/$host/skills"
  cp -R skills/stand-in "$out/$host/skills/stand-in"
done

if [ "${1:-}" = "--check" ]; then
  status=0
  while IFS= read -r -d '' f; do
    rel=${f#"$out"/}
    if ! cmp -s "$f" "$rel"; then
      echo "out of date: $rel" >&2
      status=1
    fi
  done < <(find "$out" -type f -print0)
  [ "$status" -eq 0 ] && echo "adapters are in sync"
  exit "$status"
fi

rm -rf .swival/skills/stand-in .openclaw/skills/stand-in
cp -R "$out"/. .
echo "adapters regenerated"
