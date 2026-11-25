"""Your Week in One Line — variant C (3am on-call week).

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt first, then
best-effort to a repo-root copy (the grader sandbox mounts the repo
read-only, so the root copy must never crash the run).
"""

import os

ENTRY_TEXT = "Paged at 3am: prod down. One-line fix by 4am \u2014 my own typo. My agent filed the incident against me."


def get_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir: str) -> str:
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    return path


def copy_to_repo_root() -> None:
    try:
        root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(root, "w", encoding="utf-8") as f:
            f.write(ENTRY_TEXT)
    except OSError:
        pass


def main() -> None:
    write_entry(get_output_dir())
    copy_to_repo_root()


if __name__ == "__main__":
    main()
