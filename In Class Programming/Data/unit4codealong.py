import numpy as np

py = [1,2,3]
print(py*2)

b = 25
print(np.sqrt(b)) # should output 5.0

arr2 = np.array([[1,3,5,7],[2,4,6,8]])
print(arr2)

# number of dimensions?
print(arr2.ndim)

# shape of the array?
print(arr2.shape)

MyArray = np.arange(start = 1, stop = 10, step = 2)
print(MyArray)

MyArray = np.arange(start = 1, stop = 10, step = 3)
print(MyArray)

print(arr2.dtype)
