"""Entry for "How Many Tabs Do You Have Open?" (make.fun).

Writes the entrant's honest open-tab count to entry.txt.

Why 47: it is the count of a heavy browser user who never quite closes
anything — high enough to raise an eyebrow, odd and specific enough to
sound counted rather than invented, and small enough to stay a real,
lived-in number instead of a figure picked to shock.
"""

import os
from pathlib import Path

TAB_COUNT = 47


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(f"{TAB_COUNT}\n", encoding="utf-8")


if __name__ == "__main__":
    main()
