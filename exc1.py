from collections import *

#this program find all words that contains same characters in a list
def get_anagrams(words):
    normalized = [''.join(sorted(w)) for w in words]

    d = Counter(normalized)

    return [w for w, n in zip(words, normalized) if d[n] > 1]

print(get_anagrams(["pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop"]))
