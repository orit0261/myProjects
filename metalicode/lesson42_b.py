def func_c():
    def func_d():
        nonlocal y
        y=50
    y=10
    print(f"y before func_d y={y}")
    func_d()
    return f"y after finc_d y={y}"

print(func_c())