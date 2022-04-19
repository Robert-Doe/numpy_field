import numpy as np

array_1=np.arange(10).reshape((5,2))+1
print(array_1.sum())
print(array_1.sum(axis=1)) #Sum of items in row
print(array_1.sum(axis=0)) #Sum of items in column
print(array_1.mean(axis=0,dtype=np.float))