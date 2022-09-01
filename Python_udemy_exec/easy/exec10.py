def get_fibonacci(n : int) -> int:
    # to-do
   if (n>=0):
       if n<=1:
           return n
       prev = 0
       curr = 1
       for _ in range(n-1):
          prev,curr = curr, prev + curr
       return curr
   return -1

print(get_fibonacci(7))