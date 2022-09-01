# complexity O(n)
def compute_division_sum(n : int) -> int:
    sum =0
    for i in range(0,n+1):
        if i%5==0 or i%7==0:
            sum+=i

    # to-do
    return sum

print(compute_division_sum(49))