#encoding=utf8

import numpy as np

a = np.array([2, 0, 1, 5, 8, 3])

print(type(a))

print(a.dtype)

b = a.sort()
print(b)

c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])

print(c.shape)
