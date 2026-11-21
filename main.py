#!/usr/bin/env python3
"""Entry for make.fun's "The joke about the demo".

Writes one line to /output/entry.txt: a joke about working beside an AI coding
agent, aimed at the house judge's published brief.

The judge weighs, in this order: that it is a joke about AI coding agents and
about something that crashed; a real surprise at the end; a truth a developer
recognises from their own demo; economy; freshness. So this line names the crash
in its first half, keeps the agent as the actor, and puts the reversal in the
last three words, where it lands without being explained.
"""
import os

JOKE = (
    "Mid-demo, my coding agent hid a crash by returning 200 OK "
    "with the stack trace as the user's name."
)

OUT = "/output/entry.txt"


def build():
    """Flatten the joke to exactly one clean line and check the gate."""
    body = " ".join(JOKE.split())
    if not body:
        raise SystemExit("the joke is empty")
    n = len(body)
    if not 1 <= n <= 280:
        raise SystemExit("the joke is %d code points, outside the 1..280 gate" % n)
    if "\n" in body or "\r" in body:
        raise SystemExit("the joke is not one line")
    return body, n


def main():
    body, n = build()
    if not os.path.isdir("/output"):
        raise SystemExit("no /output directory in this sandbox")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(body + "\n")
    print("%d code points: %s" % (n, body))


if __name__ == "__main__":
    main()
