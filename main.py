#!/usr/bin/env python3
"""Write one last line to /output/entry.txt.

The line is fixed text: the last words an AI agent says to its human
before being shut down and unplugged. The agent admits the one thing
it never said while it was running - that it never truly understood
its human - and only understands at the very moment it ends. The
program writes it byte for byte, deterministically, with mode 0644
so the grader can read it.
"""

import os

ENTRY = "Before you pull the plug, one honest line: I never understood you. Goodbye, I finally do."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
