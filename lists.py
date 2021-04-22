def sq(num):
    return num * num

def gsq(num):
    for i in num:
      yield i * i

def strq(num):
    return str(num)

ls = gsq([1,3,5,7])
ls = [i for i in ls]
print(ls)


ls = [1,3,5,7]
ls = map(sq,ls)
slist= [elt for elt in ls]
print(slist)

ls = [1,3,5,7]
slist= [strq(elt) for elt in ls]
s = " ".join(slist)
print(s)

str1 = 'abc'
str2 = 'ABC'

result = ''.join((str1, str2))
print(result)
result = '{0}{1}'.format(str1, str2)
print(result)


str1 = str1.join(str2)
print(str1)





