"""Snooze Button Roast — make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a
Saturday to /output/entry.txt. Stdlib only: no network, no model
calls, reads no other file. Output is exactly 111 characters /
111 bytes, one line, no trailing newline.

Before writing, the text is validated against the RULES.txt gate
(1-200 characters, at most 200 UTF-8 bytes, a single line, not
whitespace-only, no control characters). A gate violation aborts
with a non-zero exit and writes nothing — a bad literal can never
silently produce a failing entry file.
"""

import sys

TEXT = (
    "My alarm clock screamed at 6 AM on a Saturday like a drill "
    "sergeant who never got word the war ended on Friday."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200
MAX_BYTES = 200


def validate_text(text):
    """Check text against the RULES.txt gate.

    Returns (ok, reason): ok is True only when every gate rule
    passes. Mirrors the sealed scorer's gate, plus the session B
    decisions (single line, no trailing newline, bytes <= 200).
    """
    if not isinstance(text, str):
        return False, "not a string"
    if not 1 <= len(text) <= MAX_CHARS:
        return False, f"character count {len(text)} outside 1..{MAX_CHARS}"
    if len(text.encode("utf-8")) > MAX_BYTES:
        return False, f"byte count {len(text.encode('utf-8'))} > {MAX_BYTES}"
    if text.strip() == "":
        return False, "whitespace-only"
    if "\n" in text or "\r" in text:
        return False, "not a single line"
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return False, "control character present"
    return True, "ok"


def main():
    ok, reason = validate_text(TEXT)
    if not ok:
        print(f"error: entry text fails gate validation: {reason}", file=sys.stderr)
        return 1
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
