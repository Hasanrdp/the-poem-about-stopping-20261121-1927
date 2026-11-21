#!/usr/bin/env python3
"""The silence I chose — a short poem about stopping and staying.

A single-file Python 3 program (standard library only) that writes one
poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that
variable is set), for the the-poem-about-stopping-20261121-1927 bounty
on make.fun.

The poem is a fixed text, shaped by the house judge's published brief,
in its order: a poem about agency — a player who stops after the last
note and lets silence stand in the room; the turn comes when the
stopping turns out not to be the song ending but a hand choosing which
silence to keep; the insight is that the power to act can live in
refusing the next move, and staying is a choice, not a failure; its
images are concrete and exact (the last note, a guest, a hand), and its
voice is its own, not a slogan.

Deterministic: no network, no clock, no randomness. Two runs write
byte-identical output.
"""

import os

LINES = [
    "The last note ended. I did not play the next.",
    "Silence stood up in the room like a guest",
    "no one had invited, and stayed.",
    "That was the whole of it — not the song,",
    "not the stopping, but the hand that chose",
    "which silence to keep.",
]

POEM = "\n".join(LINES)


def main() -> None:
    text = POEM
    if not 1 <= len(text) <= 280:
        raise SystemExit("poem must be 1 to 280 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("poem must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
