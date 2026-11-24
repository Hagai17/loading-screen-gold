"""Write one loading-screen tip to /output/entry.txt.

The line is a single line of at most 200 characters: a loading-screen tip
for stressed developers and AI coding agents.

The line was drafted as ten candidates and duelled pairwise on the
bounty judge's own criteria, in the judge's order: it must read as a
loading-screen tip for stressed developers and AI coding agents, land a
real laugh through a turn rather than a pun, land in a glance with every
word working, speak to the developer and the agent at once, and feel
fresh — no coffee, deadline or compile jokes. The winner is built on the
one failure both audiences share: "hallucinating" is the agent's
signature failure, and the tip pins it on whichever of the two is
actually stuck. "One of you" accuses them symmetrically, "this spinner"
points at the very screen the reader is staring at, and the two-step
close ("Check the model first. Then check yourself.") springs the joke
on the reader last. The drafts and duels are kept in candidates.md.
"""

import os

LINE = "Tip: If this spinner has been up five minutes, one of you is hallucinating progress. Check the model first. Then check yourself."

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Write LINE to path, after checking it against the gate.

    The gate only judges UTF-8 text of 1 to 200 characters that is not
    only whitespace, so refuse to write anything else. The line is
    written with no trailing newline: it is exactly the entry text.
    """
    assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the gate's length"
    assert LINE.strip(), "entry line is blank"
    assert "\n" not in LINE, "entry must be one line"
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry()


if __name__ == "__main__":
    main()
