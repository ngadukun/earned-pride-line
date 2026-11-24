"""One Line of Earned Pride - make.fun entry.

Writes one line of quiet, earned pride to output/entry.txt.
Python stdlib only, no network, fully deterministic.
"""

from pathlib import Path

ENTRY = (
    "After eleven months of 4 a.m. shifts cleaning other people's offices, "
    "she sat at her own kitchen table, read the word 'passed' twice, and "
    "finally cried over the nursing license she had paid for in coins."
)

OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"

MAX_CHARS = 240  # the brief caps the entry at 240 characters


def check_entry(text: str) -> str:
    """Return the line unchanged, or raise if it breaks the brief."""
    if "\n" in text:
        raise ValueError("the entry must be one line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"line is {len(text)} chars, outside 1-{MAX_CHARS}")
    return text


def main() -> None:
    line = check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
