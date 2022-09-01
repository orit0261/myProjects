def count_vowels(input : str) -> int:
    # to-do
    count=0
    set1 = {'a','e','o','i','u'}
    input = input.lower()
    for s in range(len(input)):
        if input[s] in set1:
            count += 1
    return count

print(count_vowels('a144eb'))