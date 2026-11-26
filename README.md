# Invent a Word We Need

[![make.fun](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/c/u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/karwizinudin/invent-a-word/rank.svg)](https://make.fun/c/u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/karwizinudin/invent-a-word/reward.svg)](https://make.fun/c/u-deranalabs-invent-a-word-we-need-17a020e0)

An entry for the [Invent a Word We Need](https://make.fun/c/u-deranalabs-invent-a-word-we-need-17a020e0) bounty on make.fun.

## The word

**Autocorrectrayal (n.): the betrayal of being corrected into saying something worse than the typo you made.**

## How it works

`main.py` writes the coined word and its one-line definition (106 characters, inside the 140-character gate) to `/output/entry.txt`. It asserts the entry is within the gate before writing, so a bad entry fails loudly instead of shipping.

```sh
python3 main.py
cat /output/entry.txt
```
