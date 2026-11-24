"""One letter: coffee or tea. A for coffee, B for tea.

Coffee never asks if you're ready. Neither does a good answer.
The letter A: first in line, first to arrive, first to wake you up.
"""

import os
import sys

output_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

entry_path = os.path.join(output_dir, "entry.txt")
with open(entry_path, "wb") as f:
    # A for coffee — the only drink that matches the urgency of a deadline.
    f.write(b"A")

# Verify: exactly one byte, no newline, the letter A.
with open(entry_path, "rb") as f:
    content = f.read()
    assert content == b"A", f"Expected b'A', got {content!r}"
    assert len(content) == 1, f"Expected 1 byte, got {len(content)}"
