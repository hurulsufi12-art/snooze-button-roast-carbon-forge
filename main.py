"""Snooze Button Roast — make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a
Saturday to /output/entry.txt. Stdlib only: no network, no model
calls, reads no other file. Output is exactly 111 characters /
111 bytes, one line, no trailing newline.
"""

TEXT = (
    "My alarm clock screamed at 6 AM on a Saturday like a drill "
    "sergeant who never got word the war ended on Friday."
)

with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
