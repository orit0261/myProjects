def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.95, 2))


def by_value(item):
    return item[1]


prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# This is because .keys() returns a dictionary-view object, which yields keys on demand one at a time, and if you delete an item (del prices[key]), then Python raises a RuntimeError, because you’ve modified the dictionary during iteration.
# for key in prices.keys():
for key in list(prices.keys()):  # Use a list instead of a view
    if key == 'orange':
        del prices[key]

print(prices)

objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a_dict = {key: value for key, value in zip(categories, objects)}
print(a_dict)

incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
for key in sorted(incomes):
    print(key, '->', incomes[key])

print("sort by value")
for k, v in sorted(incomes.items(), key=by_value, reverse=True):
    print(k, '->', v)

for value in sorted(incomes.values()):
    print(value)

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
new_prices = dict(map(discount, prices.items()))
print(new_prices)


fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
# How to use the unpacking operator **
# You can use this feature to iterate through multiple dictionaries
for k, v in {**vegetable_prices, **fruit_prices}.items():
    print(k, '->', v)


number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting iterator to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)
# Converting iterator to set
result_set = set(result)
print(result_set)


words = ['apple','bread','potato','apple']
wdict = {}
for word in words:
    try:
        wdict[word] += 1
    except KeyError:
        wdict[word] = 1

print(wdict)

wdict = {}
get = wdict.get
for word in words:
    wdict[word] = get(word, 0) + 1
print(wdict)

from collections import defaultdict

wdict = defaultdict(int)
for word in words:
    wdict[word] += 1
