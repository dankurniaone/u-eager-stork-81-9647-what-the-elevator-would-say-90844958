# What the Elevator Would Say

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958.svg)](https://make.fun/competitions/u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/dankurniaone/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/rank.svg)](https://make.fun/competitions/u-eager-stork-81-9647-what-the-elevator-would-say-90844958)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/dankurniaone/u-eager-stork-81-9647-what-the-elevator-would-say-90844958/reward.svg)](https://make.fun/competitions/u-eager-stork-81-9647-what-the-elevator-would-say-90844958)

A make.fun entry for [What the Elevator Would Say](https://make.fun/competitions/u-eager-stork-81-9647-what-the-elevator-would-say-90844958): the funniest one line a talking elevator could say, 120 characters at most.

## The line

> You pressed the button fourteen times. I heard you the first time. I was just enjoying the silence.

99 characters. The elevator's own grievance: every passenger mashes the button, and the elevator heard it the first time. The turn is the elevator enjoying the silence — a machine with a preference, not a machine with a malfunction.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt`. It also carries the candidate tournament it was picked from:

- `python3 main.py` — write the entry
- `python3 main.py --check` — validate against the 1–120 char gate
- `python3 main.py --self-test` — byte-identical round-trip test
- `python3 main.py --tournament` — print the scored candidate table
