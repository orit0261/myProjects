import pytest

def test_sum(*arg):
    total = 0
    for val in arg:
        total+=val
    return total

assert test_sum(1,2,3)==sum([1,5,3])
