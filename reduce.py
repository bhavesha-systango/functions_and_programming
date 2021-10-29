from functools import reduce
import operator
result4 = reduce(operator.add, [1,2,3,4,5])
print(result4)

def mul(x, y):
    print('mul {} {}'.format(x, y))
    return x*y

print(reduce(mul, range(1,10)))
