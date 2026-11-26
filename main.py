#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in its own defence after
knocking a glass off the table, to /output/entry.txt. Standard library
only, no network, deterministic.

The angle: a territorial cat that does not apologise and does not confess.
The glass parked itself in the cat's sunbeam, on the cat's table, and gave
the cat that look — so the cat evicted it, and the floor is its new address
now. No gravity joke, no slippery edge, no "it was already falling".
"""
import os

EXCUSE = "That glass parked itself in my sunbeam, on my table, and gave me that look, so I evicted it \u2014 the floor is its new address now."


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} characters"
    assert "\n" not in text, "excuse must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
