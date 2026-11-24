"""Famous Last Words at 1 Percent: writes the entry text to /output/entry.txt.

Why this line: Phone voice throughout; doomscrolling at 2 a.m. with 47 tabs open, zero regrets, is the sting.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'Tell the charger I loved it. Tell the group chat I died doing what I loved: doomscrolling at 2 a.m. with 47 tabs open and zero regrets.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
