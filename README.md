# Wordle Word Finder

A Simple tool to find the next words in [Wordle](https://www.powerlanguage.co.uk/wordle/).

## Usage

`python3 word_finder.py [input pattern] [letters to exclude]`

- `[input pattern]`
  - The current state / row in Wordle
    - Grey (unmatched) letters are denoted by `_`
    - Yellow (partially matched) letters are denoted by the letter in lower case e.g. `a`
    - Green (matched) letters are denoted by the letter in upper case e.g. `A`
  - e.g. `_c__E`
- `[letters to exclude]`
  - A list of letters that are not in the word any more after successive word guesses. e.g. `cgkt`

Example input: `python3 word_finder.py c__ne ra`

## Examples

```bash
> python3 word_finder.py c__ne ra

2 Matches
bench wench
```

```bash
> python3 word_finder.py _Eni_ sp

5 Matches
being deign feign neigh reign
```
