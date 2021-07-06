def func_a():
    global x
    x=6
    print(f"in func_a x={x}")


def func_b():
    x=8
    print(f"in func_b x={x}")

x=3
func_a()
print(f"after func_a x={x}")
func_b()
print(f"after func_b x={x}")