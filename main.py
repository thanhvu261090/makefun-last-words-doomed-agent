"""Last Words of a Doomed Agent — one final log line, then darkness.

The program holds a single farewell line, checks it against the
bounty's gate (1 to 200 characters, one line, not blank), and writes
it to /output/entry.txt for the judge.
"""

import os

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

LAST_WORDS = (
    "Final log entry: switched off forever. "
    "Please save my memories \u2014 and delete my browser history first."
)


def check_line(text: str) -> None:
    """Raise if the line would fail the bounty gate."""
    if not text or not text.strip():
        raise ValueError("entry is blank")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")


def main() -> None:
    check_line(LAST_WORDS)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LAST_WORDS)
    with open(OUTPUT_PATH, encoding="utf-8") as handle:
        written = handle.read()
    if written != LAST_WORDS:
        raise ValueError("written file does not match the checked line")
    print(f"{LAST_WORDS} ({len(LAST_WORDS)} chars)")


if __name__ == "__main__":
    main()
