"""One-line entry for make.fun's "Real-Life Patch Notes" bounty.

A terse software patch note for a bug in human memory: entering a room
silently discards the reason you came in, and the fix ships with a known
issue admitting the reason is still gone. The comedy is the release-note
register applied to a bug no update can ever fix — the "fix" fixes nothing,
and the known issue is the punchline.
"""

import os
import sys

# The entry: one line, at most 160 characters.
# Angle: memory/forgetting — the doorway effect, written as a changelog fix.
TEXT = (
    "v2.4.1: fixed a bug where entering a room silently discarded the "
    "reason you came in. Known issue: the reason is still unrecoverable."
)


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if not (1 <= len(TEXT) <= 160):
        print(f"gate failed: entry is {len(TEXT)} characters, must be 1-160",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in TEXT or "\r" in TEXT:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(TEXT)} characters -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
