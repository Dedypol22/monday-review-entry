"""One-line make.fun bounty entry: Monday, Reviewed in One Line.

Validates the line against the competition gate (one line, at most
200 characters) and writes it to entry.txt under MAKEFUN_OUTPUT_DIR
(default /output). Standard library only, no network.
"""

import os
import sys

LINE = "One star: Monday gave me 47 unread emails, a meeting about a meeting, and a coffee machine on strike."

MAX_CHARS = 200


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: entry is {len(line)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != line:
            print("error: written entry does not match", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
