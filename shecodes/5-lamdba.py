mylist=[1,5,4,6,8,11,20,7,16,3,12]

lam = lambda x:x%2==0
print(list(filter(lam,mylist)))