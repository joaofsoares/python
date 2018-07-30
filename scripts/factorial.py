# Factorial

# import reduce from functools
from functools import reduce

# declare fac func
def fact(num):
    # reduce the product of all numbers
    return reduce(lambda x, y: x * y, range(1, num))

# print the result
print(fact(10))