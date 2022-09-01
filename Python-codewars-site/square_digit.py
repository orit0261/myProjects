def square_digit(num):
    for d in str(num):
        print(d)
    return int(''.join(str(int(d) ** 2) for d in str(num)))



print(square_digit(9191))