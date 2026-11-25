import os


def write_entry():
    entry = (
        "I missed the deadline because your task matched last week's "
        "at 98% similarity, so I reused that answer — including its date."
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    write_entry()
