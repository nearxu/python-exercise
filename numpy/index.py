import numpy as np

a ='hello world'

# print(a)

b = np.array([1,2,3,4])
c = np.array([[1,2],[3,4,[5,6]]])
# 最小维度  ndmin
d = np.array([1,2,3],ndmin =5) 
print(b)
print(c)
print(d)

#shape 多维数组维度

e = np.array([[1,2],[3,4]])
f = np.array([[1,2,3],[3,4,5]])
f.shape=(1,6)

print(e.shape)
print(f)

# reshape

# ndarray.ndim

h = np.arange(24) 
# h.ndim
i = h.reshape(2,3,4)

print(i)

j = np.empty([2,3],dtype=int)
print(j)
