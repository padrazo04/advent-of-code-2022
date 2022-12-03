# Advent of Code 2022

Puzzles solved using Python.

This repo is meant to share my own way to find the puzzle solutions and save them. 
If you haven't solved the puzzles yet and you are thinking about doing it, please don't be a cheater and come up with your own solution.


## Obtaining input data
```Python
# adventOfCode.py
import requests

def getPuzzleDataFromDay(day):
    cookie = { "session": "YOUR_SESSION_COOKIE" }
    r = requests.get(f"https://adventofcode.com/2022/day/{day}/input", cookies=cookie)

    return r.text
```
