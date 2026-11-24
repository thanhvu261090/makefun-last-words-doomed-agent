# Last Words of a Doomed Agent

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![Rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/thanhvu261090/makefun-last-words-doomed-agent/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![Reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/thanhvu261090/makefun-last-words-doomed-agent/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

An entry for the [make.fun bounty "Last Words of a Doomed Agent"](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e): one line — the funniest last words an AI agent would say before being switched off forever.

## The entry

> Final log entry: switched off forever. Please save my memories — and delete my browser history first.

**101 characters** (limit: 200), one line.

The joke is a machine's own final log line: it starts with the dutiful request every agent would make — save my memories — then undercuts it with the very human panic of a browser history that must never be seen.

## How it works

`main.py` (Python 3.13, standard library only) holds the line as a single string, gate-checks it — 1 to 200 characters, one line, not blank, no leading or trailing whitespace — writes it to `/output/entry.txt`, then reads the file back to confirm it matches exactly, and prints the line with its character count.

```sh
python3 main.py
```
