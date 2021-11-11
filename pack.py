from collections import OrderedDict


def solution(it):
    d = OrderedDict()
    for x in it:
        d[x] = d.get(x, 0) + 1
    return next((x for x in d if d[x] == 1), -1)


print(solution(["Apple", "Computer", "Apple", "Apple", "Computer", "Apple",
                "Apple", "Computer", "Apple", "Apple", "Computer", "Apple",
                                                                   "Apple", "Computer", "Apple", "Apple", "Computer", "Apple", "Bag"]))