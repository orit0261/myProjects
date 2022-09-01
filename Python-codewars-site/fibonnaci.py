def tribonacci(signature, n):
    a,b,c = signature
    if n==0 :
        return []
    if n==1:
        return [1]
    if n<3:
      lst1=[a,b]
    else:
     lst1=[a,b,c]


    for i in range(n-3):
        sum = a+b+c
        a,b,c=b,c,sum
        lst1.append(c)
    return lst1



print(tribonacci([46, 149, 30],2))