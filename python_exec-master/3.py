import heapq
import random
import collections
from collections import Counter

a = [2,2,2,1,1,1,1,5,5,5,5,5,5,5]
counter = collections.Counter(a)
print(counter)
#a=(sorted(a, key=Counter(a).get, reverse=True))
#print(a)
b=dict(sorted(counter.items(), key=lambda item: item[1]))

print(list(b.keys())[2])
print(b)



