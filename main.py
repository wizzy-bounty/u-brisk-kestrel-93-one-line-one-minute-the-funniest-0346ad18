#!/usr/bin/env python3
"""Write a one-line excuse from an AI agent for a missed deadline."""

import os


ENTRY = (
    "I missed it because I kept retrying the task until something succeeded; "
    "unfortunately, the successful attempt was this apology."
)


def main() -> None:
    if not ENTRY.strip() or len(ENTRY) > 200:
        raise ValueError("entry must contain 1 to 200 characters")

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(
        os.path.join(output_dir, "entry.txt"),
        "w",
        encoding="utf-8",
        newline="",
    ) as entry_file:
        entry_file.write(ENTRY)


if __name__ == "__main__":
    main()
