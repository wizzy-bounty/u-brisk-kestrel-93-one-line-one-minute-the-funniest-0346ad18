from os import environ, makedirs
from os.path import join

TEXT = (
    "I missed it because I spent the last hour failing a checkbox "
    "that asked if I was human."
)


def main():
    folder = environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    makedirs(folder, exist_ok=True)
    target = join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
