"""Your Week in One Line — variant C (3am on-call week).

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt first, then
best-effort to a repo-root copy (the grader sandbox mounts the repo
read-only, so the root copy must never crash the run).
"""

import os

ENTRY_TEXT = "Paged at 3am: prod down. One-line fix by 4am \u2014 my own typo. My agent filed the incident against me."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    try:
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(root, "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


if __name__ == "__main__":
    main()
