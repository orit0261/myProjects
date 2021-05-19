from heapq import merge
from multiprocessing.pool import Pool
import config
import random
import string


def get_dic():
    return {"username": config.POSTGRES_USER,
            "port": config.POSTGRES_PORT,
            "database": config.POSTGRES_DB,
            "password": config.POSTGRES_PW,
            "host": config.POSTGRES_URL
            }


# generate random string len between max and min
def generate_random_string(min_len=5, max_len=15):
    num_char = random.randint(min_len, max_len)

    rand_string = ""
    for i in range(num_char):
        rand_string += random.choice(string.ascii_letters.upper())

    return rand_string


# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def domerge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        domerge(arr, l, m, r)
        return arr




def sort_parallel(xs, n_workers):
    pool = Pool(n_workers)
    pos = [i * len(xs) // n_workers for i in range(n_workers + 1)]
    xss = [xs[i:j] for i, j in zip(pos[:-1], pos[1:])]
    pool.map(sort_inplace, xss)
    return list(merge(*xss))


def sort_inplace(xs):
    xs.sort()
# for i in range(0, 200000, 2000):
#   print(i)
# # Driver code to test above
# arr = [12, 11, 13, 5, 6, 7, -1 ,0 ,9 ,12]
# n = len(arr)
# print("Given array is")
# for i in range(n):
#     print("%d" % arr[i]),
#
# mergeSort(arr, 0, n-1)
# print("\n\nSorted array is")
# for i in range(n):
#     print("%d" % arr[i]),
