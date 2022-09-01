def is_complement_number(arr: list, target: int) -> bool:
    # to-do
    map={}
    for i in range(len(arr)):
        if (arr[i] in map.values()):
            return True
        comp= target-arr[i]
        map[i] = comp
    return False


print(is_complement_number([7,2,3,4,10],10))
