def int2bin(val):
    return bin(val)[2:].zfill(8)


print(int2bin(3))