"""Invent a Word We Need — entry for make.fun.

Coins one new English word and defines it in a single clear line
(max 140 characters), written to /output/entry.txt.
"""

import os

WORD = "Autocorrectrayal"
DEFINITION = "the betrayal of being corrected into saying something worse than the typo you made."

ENTRY = f"{WORD} (n.): {DEFINITION}"

# The gate allows 1 to 140 characters; fail loudly instead of shipping
# an entry the sealed scorer would refuse.
assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, gate allows 1-140"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
