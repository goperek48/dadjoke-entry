"""Dad Joke Showdown — entry program.

Writes one original dad joke to /output/entry.txt.

The joke, and why it is built this way:

    My son asked why I always carry spare socks.
    I said, 'In case I get cold feet.'

A dad joke has to survive being read out loud at the dinner table,
so this one is built around a single turn that needs no explaining.
The setup is a question any kid would genuinely ask — why does Dad
always have spare socks? — and the answer takes the idiom "cold
feet" at face value: socks are, literally, what you carry against
cold feet. One clean pun, one beat of setup, punchline at the end,
nothing left over. It is a father telling a joke to his son, in the
father's own voice, and the groan is the point: the joke is the
whole entry, so every word earns its place and the turn arrives
exactly where a listener expects the joke to land.
"""

from pathlib import Path

JOKE = "My son asked why I always carry spare socks. I said, 'In case I get cold feet.'"

OUTPUT_PATH = Path("/output/entry.txt")


def validate(joke: str) -> str:
    """Normalise the joke and hold it to the gate's own limits.

    The sealed scorer accepts UTF-8 text of 1 to 200 characters that
    is not only white space, so collapse any stray whitespace and
    check the length here, before anything is written, rather than
    trusting the literal by eye.
    """
    text = " ".join(joke.split())
    assert text, "joke must not be empty or whitespace-only"
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    return text


def main() -> None:
    joke = validate(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(joke, encoding="utf-8")
    print(f"Wrote dad joke ({len(joke)} chars) to {OUTPUT_PATH}")
    print(joke)


if __name__ == "__main__":
    main()
