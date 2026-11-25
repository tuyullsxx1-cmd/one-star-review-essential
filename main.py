"""Write the one-star review entry to /output/entry.txt."""

import os
from pathlib import Path

ENTRY = "One star. Sleep charges eight hours a night, offers no refund for the nightmares, and still expects a tip in the morning."


def main():
    out_dir = Path(os.getenv("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
