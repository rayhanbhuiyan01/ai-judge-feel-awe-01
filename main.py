#!/usr/bin/env python3
"""Write one short tide-and-stars text to entry.txt.

Deterministic, stdlib only, no network. Reads OUTPUT_DIR (default /output),
creates it, writes TEXT to entry.txt inside it, and prints the char count.
Before writing, the text is checked against the 1-280 character gate, and
after writing the file is read back to confirm the round trip matches.
"""

import os
from pathlib import Path

MIN_CHARS = 1
MAX_CHARS = 280


def check_text(text: str) -> None:
    """Refuse any text that falls outside the allowed character gate."""
    length = len(text)
    if length < MIN_CHARS or length > MAX_CHARS:
        raise SystemExit(
            f"Entry text is {length} characters; "
            f"it must be between {MIN_CHARS} and {MAX_CHARS}."
        )


TEXT = (
    "Past the last streetlight, the tide comes in over flat sand, "
    "slow and unhurried. Above it, more stars than the sky has room for, "
    "each one still arriving. Nothing here needs you; the water keeps its "
    "own time, and the dark goes on, watched or not."
)


def main() -> None:
    check_text(TEXT)
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(TEXT, encoding="utf-8")
    written_back = output_path.read_text(encoding="utf-8")
    if written_back != TEXT:
        raise SystemExit("Round-trip check failed: entry.txt does not match TEXT.")
    print(f"Wrote {len(TEXT)} characters to {output_path}")


if __name__ == "__main__":
    main()
