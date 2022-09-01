import collections


def list_duplicate_numbers(arr : list) -> list:
    # to-do
    repeats = [ item for item,count in collections.Counter(arr).items()
                if count==2]
    return repeats

print(list_duplicate_numbers([1,3,4,3,2,1]))