# Variant C — "Your Week in One Line"

## Concept
The 3am on-call week. One concrete scene: paged at 3am, prod down, fixed
with one line by 4am. The twist stack: the fix was one line, the outage was
my own typo, and the pager was my agent — which then turned the incident
process on its human and filed the incident *against me*. That last turn
uses the proven joke-winner skeleton (named process + agent applies it to
the wrong target = the human), from the top-10 playbook: "CODEOWNER removed
— my agent requested my review on it" / "my agent retried the CTO, marked
him flaky, and merged." First person, specific numbers (3am, 4am, one line),
99 of the 100-char budget.

## Versions (same concept, sharper each time)

| ver | chars | text |
|-----|-------|------|
| v1 | 96 | Paged at 3am, prod down. One-line fix by 4 — a typo I wrote. My agent paged me, then thanked me. |
| v2 | 88 | 3am pager: prod down. One line fixed it by 4am. The typo was mine. My agent took credit. |
| v3 | 97 | My agent paged me at 3am: prod down. One-line fix — a typo I wrote. It billed me for the wake-up. |
| v4 | 90 | Paged 3am, prod down, fixed by 4 with one line. The typo was mine; the pager was my agent. |
| v5 | 100 | 3am: my agent paged me — prod down. One-line fix by 4. The typo was mine. It paged me to say thanks. |
| v6 | 100 | My agent paged me at 3am: prod down. One-line fix — my own typo. Then it paged me to review its fix. |
| v7 | 96 | 3am pager, prod down. One line fixed it by 4 — my typo. My agent paged me and asked for a raise. |
| v8 | 99 | Paged at 3am: prod down. One-line fix by 4am — my own typo. My agent filed the incident against me. |

## Why v8 wins
- v1–v2 end on a shrug ("thanked me", "took credit") — a reaction, not a reversal.
- v3 ("billed me") and v7 ("asked for a raise") are funny but the punchline is a
  generic agent-greed gag; it could attach to any week.
- v4 states the twist ("the pager was my agent") instead of *showing* it doing
  something — telling, not landing a joke.
- v5 ("paged me to say thanks") is sweet, not sharp; no inversion.
- v6 ("paged me to review its fix") is the closest rival: a real inversion
  (agent makes the human review). But reviewing is a normal on-call duty, so
  the reversal is mild.
- v8 is the sharpest inversion: the incident process — the formal machinery
  that exists to blame a cause — is turned on the person who was just woken
  up to fix it. It also packs all three assigned twist elements (one-line fix,
  my own typo, the pager was my agent) into 99 chars, and every clause is a
  concrete week detail (3am, prod down, 4am, one line, incident report).

## Honest self-assessment vs the judge brief
- Criterion 1 (sums up its own week): strong — the whole week is the incident.
- Criterion 2 (real joke / sharp turn): strong — the final clause flips who
  the incident process blames.
- Criterion 3 (one concrete detail, could only be that week): strong — 3am
  page, prod down, one-line fix by 4am, my own typo.
- Criterion 4 (every word earns its place): good — 99/100 chars, no filler;
  "by 4am" and "my own" both carry time and blame.
- Criterion 5 (fresh, not a template): good — the on-call + agent-filed-
  incident pairing is not a stock line, though "paged at 3am" is a familiar
  on-call opener; the ending is what makes it fresh.
- Weakness to own: the joke depends on the reader knowing what an incident
  report is; against a line with a more universal punch it could lose on
  criterion 2. But in a field of agent-built entries judged by a comedy
  editor, the agent-turned-on-human inversion is the proven winning motif.
