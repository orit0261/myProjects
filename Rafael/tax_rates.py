def calc_tax(sum, tup_tax):
    sum_tax = 0
    left = sum
    for lower_sum, upper_sum, tax in tup_tax:
        print(lower_sum, upper_sum, tax)
        if sum > upper_sum :
            left = upper_sum-lower_sum
            sum_tax = sum_tax + (left * tax)
        elif sum > lower_sum:
            left = sum - lower_sum
            sum_tax = sum_tax + (left*tax)
    print(sum_tax)

tup_tax = [(0, 6000, 0), (6000, 8000, 0.1), (8000, 10000, 0.2), (10000, 999999, 0.3)]
calc_tax(7000, tup_tax)
