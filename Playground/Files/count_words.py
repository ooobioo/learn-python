#!/usr/bin/env python
from collections import Counter

allowed_chars = set("abcdefghijklmnopqrstuvwxyzüäöß")

with open("emil.txt", "r") as fobj:
    woerter_alle = []
    for line in fobj:
        woerter_line = line.split()
        for wort in woerter_line:
            wort = wort.strip()
            wort_gefiltert = ''.join(char for char in wort if char.lower() in allowed_chars)
            woerter_alle.append(wort_gefiltert)
    print("Gesamt Woerter:", len(woerter_alle))
    woerter_menge = list(set(woerter_alle))
    print("Einzelne Woerter:", len(woerter_menge))

    a = dict(Counter(woerter_alle).most_common(20))
    print(a)