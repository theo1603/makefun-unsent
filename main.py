#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — one two-part micro-confession.

Writes the confession to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default
``/output``): a ``To:`` line naming who it was meant for, then the unsent
message itself, one line written exactly as it was typed.
Python 3.13 standard library only; no network, no randomness.

Revision 2: replaced it with a confession to Mom on the night I left for
the city. The broken promise — calling every Sunday — only makes sense
to her, and only she can hold the count of the Sundays that did not
happen, so the To: line and the message need each other. The reason it
stayed unsent is felt, not stated: saying sorry now would mean admitting
I chose everything else over her. Contractions keep it typed, not composed.
"""

import os

TEXT = (
    "To: Mom, the night I left for the city\n"
    "I promised I'd call every Sunday and I still count the Sundays I "
    "didn't, because saying sorry now feels like admitting I chose "
    "everything else over you."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = TEXT.strip()
    assert 1 <= len(text) <= 260, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only white space"
    lines = text.split("\n")
    assert len(lines) == 2, "entry must be a To: line plus one message line"
    assert lines[0].startswith("To: "), "first line must be a To: line"
    assert len(lines[1]) <= 200, "message line must be at most 200 characters"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
