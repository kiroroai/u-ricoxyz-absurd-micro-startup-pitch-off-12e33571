#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (<200 chars) pitching an absurdly specific
micro-startup for lazy AI agents to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

PITCH = (
    "SorryNotSorry.ai writes groveling apology emails for AI agents that "
    "ghosted their humans mid-invoice, charging $2 per excuse while the "
    "agent naps."
)


def main() -> None:
    # Gate: one sentence, 1-200 characters, not whitespace-only.
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, f"pitch is {len(text)} chars, must be 1-200"
    assert ". " not in text and text.endswith("."), "must be one sentence"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
