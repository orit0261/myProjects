def get_int():
    while True:  # keep looping until we break out of the loop
        try:
            val = int(input("Please enter val:\n"))
            break  # exit the loop if the previous line succeeded
        except ValueError:
            print("Please enter an integer!")
    return val

x = get_int()
y = get_int()

print(f'You entered {x},{y}')

# if x+y returns False assert is displaying else just print wrong value
assert (x+y>10)
print("wrong value")