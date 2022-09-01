# running time O(logn)
def Search(x, arr, l, r):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return "the value Found ", str(mid)
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return "value has not been found"


print(Search(6, [0,1, 2, 3, 4, 5, 6, 7, 8], 1, 9))
