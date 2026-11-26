#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry.

Writes one line, at most 120 characters, to /output/entry.txt:
the funniest thing a talking elevator could say, in its own voice.

Tournament (specificity / surprise / freshness, each 1-5):
 1. Floor 13 doesn't exist, but I stop there anyway. The
    passengers who get off never come back.                 4/5/4 = 13
 2. I have carried 40,000 people and not one of them has
    ever said thank you to the doors.                       4/3/3 = 10
 3. You pressed the button fourteen times. I heard you the
    first time. I was just enjoying the silence.            5/5/5 = 15 WINNER
 4. Weight limit 1,000 kilos. You brought the whole office.
    I am not a truck, I am a box with ambitions.            4/4/4 = 12
 5. I go up. I go down. Nobody asks how my day is going,
    and my day is going up and down.                        3/3/2 = 8
 6. The doors are closing. So is my patience with the man
    holding them open for his sandwich.                      4/4/4 = 12
 7. You have been waiting four minutes. I have been waiting
    since 1987. We are not the same.                        5/5/4 = 14
 8. Floor 9, going up. Floor 9, going down. I have been to
    floor 9 so many times I dream in nines.                  4/4/4 = 12

The winner is the elevator's own grievance: every passenger mashes
the button, and the elevator heard it the first time. The turn is
the elevator enjoying the silence — a machine with a preference,
not a machine with a malfunction. No pun, no explanation, and the
voice could come from no other machine: only an elevator knows
what fourteen button presses feel like. The line runs 99 chars,
21 under the 120-char gate, so nothing reads cut off.
"""

import argparse
import sys
from pathlib import Path

LINE = "You pressed the button fourteen times. I heard you the first time. I was just enjoying the silence."

MAX_CHARS = 120

CANDIDATES = [
    ("Floor 13 doesn't exist, but I stop there anyway. The passengers who get off never come back.", 4, 5, 4),
    ("I have carried 40,000 people and not one of them has ever said thank you to the doors.", 4, 3, 3),
    ("You pressed the button fourteen times. I heard you the first time. I was just enjoying the silence.", 5, 5, 5),
    ("Weight limit 1,000 kilos. You brought the whole office. I am not a truck, I am a box with ambitions.", 4, 4, 4),
    ("I go up. I go down. Nobody asks how my day is going, and my day is going up and down.", 3, 3, 2),
    ("The doors are closing. So is my patience with the man holding them open for his sandwich.", 4, 4, 4),
    ("You have been waiting four minutes. I have been waiting since 1987. We are not the same.", 5, 5, 4),
    ("Floor 9, going up. Floor 9, going down. I have been to floor 9 so many times I dream in nines.", 4, 4, 4),
]


def check(line=LINE):
    """Gate: UTF-8, 1-120 chars, not only whitespace."""
    if not line or not line.strip():
        return False, "empty or whitespace only"
    if len(line) > MAX_CHARS:
        return False, f"{len(line)} chars exceeds {MAX_CHARS}"
    line.encode("utf-8")
    words = len(line.split())
    return True, f"{len(line)} chars, {len(line.encode('utf-8'))} bytes, {words} words, 1 line"


def write_entry(outdir="/output"):
    out = Path(outdir) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    return out


def tournament():
    rows = sorted(CANDIDATES, key=lambda c: (c[1] + c[2] + c[3]), reverse=True)
    for i, (text, spec, surp, fresh) in enumerate(rows, 1):
        print(f"{i}. [{spec}/{surp}/{fresh} = {spec + surp + fresh}] {text}")
    best = rows[0]
    print(f"\nWinner: {best[0]}")


def self_test():
    ok, msg = check()
    assert ok, msg
    tmp = Path("/tmp/elevator-self-test")
    p = write_entry(str(tmp))
    assert p.read_text(encoding="utf-8") == LINE, "round-trip mismatch"
    assert len(LINE) <= MAX_CHARS
    print("self-test OK:", msg)


def main(argv=None):
    parser = argparse.ArgumentParser(description="What the Elevator Would Say")
    parser.add_argument("--check", action="store_true", help="validate the line against the gate")
    parser.add_argument("--self-test", action="store_true", help="byte-identical round-trip test")
    parser.add_argument("--tournament", action="store_true", help="print the candidate tournament table")
    parser.add_argument("--outdir", default="/output", help="output directory (default /output)")
    args = parser.parse_args(argv)

    if args.tournament:
        tournament()
        return 0
    if args.check:
        ok, msg = check()
        print(("VALID: " if ok else "INVALID: ") + msg)
        return 0 if ok else 1
    if args.self_test:
        self_test()
        return 0

    out = write_entry(args.outdir)
    print(f"wrote {out} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
