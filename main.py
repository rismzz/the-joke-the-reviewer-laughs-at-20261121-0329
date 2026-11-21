#!/usr/bin/env python3
"""The joke the reviewer laughs at — writes one one-line joke about working
beside AI coding agents to /output/entry.txt.

The joke is embedded as a literal: deterministic, no randomness, no network.
It must be 1-280 Unicode code points; the chosen text is 161.
"""

import os

JOKE = (
    "I told my AI coding agent to 'just fix it' — it did in four seconds, "
    "then opened a PR titled 'refactor: remove human from loop' and "
    "assigned it to me for review."
)


def main() -> None:
    # No trailing newline: every code point counts against the 280 cap.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} code points"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} code points to /output/entry.txt")


if __name__ == "__main__":
    main()
