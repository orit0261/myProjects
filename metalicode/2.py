string = list('The quick brown fox jusmps over the lazy dog')
result = []
for i in string:
        if i == 'o':
                i = '0'
        result.append(i)
print(''.join(result))

str1 = "i am a string with space"

mystr=str1
print(mystr[:-1].zfill(40)[::-1])

#print(str1.split())
print('#'.join(mystr))

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

raise Exception("hohfgph")