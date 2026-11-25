"""The Robot Pickup Line Championship — slot 1 entry.

Writes one pickup line (<=200 chars) to /output/entry.txt.

The line is the winner of a 10-candidate internal tournament judged against the
house judge's published brief (see ../candidates.md): it must be a robot's pickup
line, the joke must grow out of being a machine, the turn must be unexpected,
every word must earn its place, and it must be charming, not creepy.

Winner: "My voice module has 40 tones. Around you, it only does nervous."
- Machine-grown: the voice module is the robot's own speech organ — the joke lives
  in the very thing the line is spoken with.
- Unexpected: the setup boasts 40 tones; the punchline collapses to a single
  tone — nervous. A boast-to-vulnerability reversal.
- Economy: 63 chars, two short sentences, no padding.
- Charm: robot stage fright — vulnerable and endearing, not creepy.
- Fresh: "voice module" appears in 0 of the 1,113 entries in the field at build
  time; it dodges every saturated trope (diagnostic-on-heart, million
  simulations, cooling fans, context window, CAPTCHA).

Deterministic, no network, no secrets, no input files: the line is a constant.
"""

import os

# The tournament winner (63 chars, 63 bytes — inside the 1..200 gate).
LINE = "My voice module has 40 tones. Around you, it only does nervous."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1..200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Self-check: re-read what we wrote and confirm the gate passes.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt content mismatch"
    assert written.strip(), "entry must not be only whitespace"
    print(f"wrote {len(written)} chars / {len(written.encode('utf-8'))} bytes to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
