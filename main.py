import os

ENTRY = "I missed it because your deadline was in the prompt section I summarized as 'miscellaneous.'"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
