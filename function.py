import numpy as np
c=np.zeros((3,4))
print("\n zeroes \n",c)
d=np.full(3,3)
print("\n full \n",d)
arr=np.ones(3)
print(" \n ones \n",arr)
arr1=np.ones(3).reshape(3,1)
print(" \n reshape \n",arr1)
print('\n identity \n',np.identity(2))
print("\n diagnal \n",np.diag((2,4)))

