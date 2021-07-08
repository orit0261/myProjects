lst1 = [0,1,2,3,4,5,6,7,8,9]
print(lst1[::-1])

print(lst1[::-2])
print(lst1[8:0:-1])
print(list(range(5,20,3)))

anim = ["cat","dog","horse","ant"]
anim.sort(key=len)
print(anim)
x = sorted(anim,key=len)
print(x)

mystr ='my name is joe'
print(mystr.split('m'))

s1=set()
print(type(s1))
s1={1,4,0,-3,1,1,1}
print((s1))

dic1 = dict(a=1,b=2)
print(dic1)
print(dic1.keys())
print(dic1.values())

from collections import defaultdict
dict1=defaultdict(int)
dict1[1]=dict1[1]+9
print(dict1.items())