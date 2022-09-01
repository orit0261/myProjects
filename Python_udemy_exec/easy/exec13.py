def sort(arr : list) -> list:
    # to-do
    for i in range(len(arr)):
        for j in range(i):
            if arr[i]<=arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr


print(sort([2,4,1,3,5]))