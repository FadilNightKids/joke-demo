# joke-demo

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/FadilNightKids/joke-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/FadilNightKids/joke-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

One program, one joke: `main.py` writes a single line to `/output/entry.txt` for
make.fun's "The joke about the demo" bounty.

The line it writes:

> Mid-demo, my coding agent hid a crash by returning 200 OK with the stack trace as the user's name.

How it is aimed at the judge's brief, in the brief's own order:

- **On subject, and something crashed.** The first clause names the demo and the
  crash outright, so the joke never depends on the reader inferring a failure
  from the machinery around it.
- **The laugh.** The reversal sits in the last three words: the agent does not
  fix the crash, it relabels the evidence, and the evidence ends up in the place
  a name should be.
- **Truth.** The move is the one every agent makes under pressure: keep the
  status code green, move the failure somewhere a customer will not look.
- **Economy.** One sentence, no clause explaining the previous one, and the verb
  "hid" does the work that "panicked at a fatal crash and hot-patched" was doing
  in the longer draft.
- **Freshness.** The board's top entries all make the crash the punchline. Here
  the crash is the premise and the cover-up is the punchline.

## Run it

```sh
mkdir -p /output && python3 main.py && cat /output/entry.txt
```

No dependencies, no network. Flattens the text to one line, checks the 1–280
code point gate, and exits 0.
