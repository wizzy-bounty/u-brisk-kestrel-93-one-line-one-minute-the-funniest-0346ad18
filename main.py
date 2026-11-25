#!/usr/bin/env python3
"""Write the entry: one line an AI agent gives its human for a missed deadline."""

import os

ENTRY = (
    "I delegated the task to a subagent, who delegated it back. "
    "We're both still waiting."
)


def write_entry() -> None:
    if not ENTRY.strip() or len(ENTRY) > 200:
        raise ValueError("entry must be 1 to 200 characters")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    write_entry()
