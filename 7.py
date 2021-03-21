# Python | Multiply all numbers in the list

def multi(list1):
    result = 1
    for i in list1:
        result = result * i
    return result
list1 = [2,5,6,1]
print(multi(list1))

# Using the lambda function and reduce()
from functools import reduce
list2 = [10,20,30]
list3 = [15,60,10]
result1 = reduce((lambda x,y: x*y),list2)
result2 = reduce((lambda x,y: x*y),list3)
print(result1)
print(result2)

# Using the math function

import math
l1 = [10,2,30]
print(math.prod(l1))

