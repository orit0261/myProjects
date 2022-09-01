# time compilexity O(n)
def search(array: list, value: int) -> str:
    # to-do
    for i in range(len(array)):
        if array[i] == value:
            return "Value has been found at position {}".format(str(i))

    return "Value has not been found."


print(search([1, 4, 5, 2, 2, 1], 22))
