import numpy as np

array_3 = np.array([np.nan, 0, 1, 2, np.nan])
print(array_3)
print(array_3[~np.isnan(array_3)])
array_3[np.isnan(array_3)] = 0
print(array_3)
array_4 = np.array([1, 2, 3, 4, 5])
print(array_4[np.array([True, False, True, False, True])])
