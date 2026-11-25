#!/usr/bin/env python3
"""make.fun entry: The Meeting That Should Have Been an Email.

Writes one line about the meeting that should have been an email to
/output/entry.txt (<= 200 chars). Deterministic: fixed string, no
randomness, no clock, no network.
"""

import os

ENTRY = "This meeting could have been an email. Instead, twelve people spent an hour discovering that out loud, one slide at a time."
# Gate: entry.txt must be 1-200 UTF-8 chars, not only whitespace.
# This line is 123 chars. The joke: the meeting's only outcome was
# everyone realising, together and slowly, that it never needed to happen.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Self-check: what landed on disk must be exactly the gated line.
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY


if __name__ == "__main__":
    main()
