import numpy as np
from functools import reduce
#reshape the array size
arr=np.array([1,2,3,2,6,8,8,6,8])
re=arr.reshape((3,3))
print("reshape",re)
#create fibnacci series
fib_arr=list([1,2,3,5,8,13,21,34])
a=list(map(lambda x :x-1,fib_arr))
print(a)




