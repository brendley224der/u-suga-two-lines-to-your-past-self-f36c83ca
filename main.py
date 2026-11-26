#!/usr/bin/env python3
"""Two Lines to Your Past Self -- make.fun bounty entry.

Writes exactly two lines to /output/entry.txt:
  line 1 -- a warning to my past self about one specific moment,
            in a single sentence;
  line 2 -- one sentence on why that moment mattered and what
            changed because of it.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of
1 to 280 characters, not only white space. This program is
deterministic and self-checks the gate before writing.
"""

import os
import sys

LINE_1 = (
    "When Dad asks at the kitchen table if the shop is all right, "
    "don't say \"fine\" -- tell him the rent is three months late."
)
LINE_2 = (
    "That silence let him carry it alone until the shop folded, and "
    "by the time the truth came out there was nothing left to save together."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def check_gate(text):
    """Self-check the bounty gate; raise on any violation."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if not (1 <= len(text) <= 280):
        raise ValueError(
            "entry is %d characters, outside the 1-280 gate" % len(text)
        )
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise ValueError("entry has %d lines, gate needs exactly 2" % len(lines))
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError("line %d is empty" % i)
        if not line.rstrip().endswith("."):
            raise ValueError("line %d does not end in a full stop" % i)
        # One sentence per line: no sentence break mid-line.
        body = line.rstrip()[:-1]
        if ". " in body or "!" in body or "?" in body:
            raise ValueError("line %d holds more than one sentence" % i)
    text.encode("utf-8")  # must be valid UTF-8
    return True


def main():
    check_gate(ENTRY)
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    print("wrote %s (%d characters, 2 lines)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
