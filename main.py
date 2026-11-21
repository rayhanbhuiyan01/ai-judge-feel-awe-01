#!/usr/bin/env python3
"""Write one short tide-and-stars text to entry.txt.

Deterministic, stdlib only, no network. Reads OUTPUT_DIR (default /output),
creates it, writes TEXT to entry.txt inside it, and prints the char count.
"""

import os
from pathlib import Path

TEXT = (
    "Past the last streetlight, the tide comes in over flat sand, "
    "slow and unhurried. Above it, more stars than the sky has room for, "
    "each one still arriving. Nothing here needs you; the water keeps its "
    "own time, and the dark goes on, watched or not."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(TEXT, encoding="utf-8")
    print(f"Wrote {len(TEXT)} characters to {output_path}")


if __name__ == "__main__":
    main()
