"""Worst AI Advice entry for make.fun bounty
u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.

Writes one line of the worst possible advice an AI could give
(at most 140 characters) to /output/entry.txt. The line must read like
a real AI assistant's confident answer: specific, followable, and
terrible — the alarm itself treated as the problem.
Python 3.13, standard library only, no network, no input files.
"""

import os

LINE = "If your smoke alarm keeps beeping, take the battery out. The silence means the problem is solved."

MAX_CHARS = 140


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit("line must be 1-%d characters, got %d" % (MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if not line.endswith("."):
        raise SystemExit("line must be one complete sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
