from functools import reduce

print(reduce(lambda x,y: x+y, [1,2,3,4,5,6,7]))


def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))
print(factorial(5))