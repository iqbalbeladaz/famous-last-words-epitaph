#!/usr/bin/env python3
"""What Could Possibly Go Wrong? — entry program.

Writes one line, the funniest famous last words as a tombstone epitaph,
to /output/entry.txt. Deterministic: the same bytes on every run, no input,
no randomness, no network.

The epitaph: "Here lies the man who asked, 'What could possibly go wrong?'
— This." The joke turns on the most famous last words ever spoken — the
rhetorical question everyone asks right before disaster — and the twist is
that the tombstone itself is the answer: the stone you are reading IS what
went wrong. The setup is his dying speech, the punchline is the grave.
"""

from pathlib import Path

ENTRY = (
    "Here lies the man who asked, 'What could possibly go wrong?' — This.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 150 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 150, "entry must be 1-150 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    # Verify what was written before returning: the gate reads this file.
    written = out.read_text(encoding="utf-8")
    assert written == ENTRY, "entry.txt does not match the entry"
    assert written.count("\n") == 1, "entry must be exactly one line"


if __name__ == "__main__":
    main()
