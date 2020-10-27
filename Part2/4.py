from functools import reduce
  
fib = lambda n: reduce(lambda i, _: i+[i[-1]+i[-2]],range(n-2), [0, 1]) 
  
print(fib(7))
