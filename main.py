#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes one deadpan excuse from a robot vacuum to /output/entry.txt
(UTF-8, 127 Unicode code points, inside the 1-200 character gate).
Deterministic, standard library only, no network, no environment reads.

The line: the vacuum's lidar classified a single crumb as a
load-bearing feature of the floor, so per protocol it refuses to
demolish architecture. Deadpan machine voice, smug about its sensors,
a specific surprise turn, and the punch lands on the last word.
"""

import os

TEXT = (
    "My lidar mapped that crumb as a structural load-bearing feature "
    "of the floor and, per protocol, I do not demolish architecture."
)


def main() -> None:
    # The grader mounts /output; create it defensively for local runs too.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
