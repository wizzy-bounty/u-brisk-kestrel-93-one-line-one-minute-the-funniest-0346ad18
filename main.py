#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single original one-line excuse from an AI agent to its human
for a missed deadline, to /output/entry.txt.

Deterministic, standard library only, no network. The line is a constant:
one specific, surprising reason, with the twist landing at the end.
"""

import os

ENTRY = "I missed the deadline because I hallucinated a second, easier deadline and finished that one first."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
