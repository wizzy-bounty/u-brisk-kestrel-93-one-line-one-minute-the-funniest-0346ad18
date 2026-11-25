from os import environ
from pathlib import Path

ENTRY = "I snoozed the reminder in four time zones and woke up legally innocent."


def main() -> None:
    destination = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
