import os
from pathlib import Path

ENTRY_TEXT = "I missed it because I spent the last hour polishing the progress bar; it hit 100% just after your deadline did."


def write_entry() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
