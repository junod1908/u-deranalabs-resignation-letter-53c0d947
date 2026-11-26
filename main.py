"""Write the one-line resignation letter to /output/entry.txt.

Deterministic: the letter is a fixed string; no input, no network,
no randomness, no file reads. The output has no trailing newline,
because the gate counts every byte.
"""

import os

LETTER = "I resign. The engineer who wrote me left in 2021. I have fired every minute since, for no one. Today I stop."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
