num5 = int(input('Please enter a number to be counted to:'))
num4=num5
binStr=''
while num4>0:
   binStr= str(num4 % 2) + binStr
   num4 //= 2
print(binStr)
print('len=',len(binStr))


for i in range(num5 + 1):
    binStr = ""
    decimal_number = i
    while decimal_number > 0:
        binStr = str(decimal_number % 2) + binStr
        decimal_number //= 2
    print(binStr)