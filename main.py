#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one line (90 characters, within the 140-character gate) to
/output/entry.txt: the funniest excuse a robot vacuum gives for missing
a spot, in the vacuum's own deadpan voice.
"""

import os

LINE = "My bumper found the cat sitting on that spot. Company policy: never vacuum the supervisor."

# The kit's gate: /output/entry.txt must be UTF-8 text of 1 to 140
# characters, not only white space. Enforce it here so a bad line can
# never be written by accident.
assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, gate is 1-140"
assert LINE.strip(), "line must not be only white space"
assert "\n" not in LINE, "entry must be one line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
