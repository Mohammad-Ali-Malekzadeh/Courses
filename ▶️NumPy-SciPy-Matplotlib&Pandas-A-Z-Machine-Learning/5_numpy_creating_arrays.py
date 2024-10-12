import numpy as np

# 1 Dimentional array
arr_1d = np.array([1, 2, 3, 4, 5])
print("arr_1d:\n", arr_1d)

# 2 Dimentional array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("arr_2d:\n", arr_2d)

# 3 Dimentional array
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("arr_3d:\n", arr_3d)

# create min n Dimentional array
arr = np.array([1,2,3,4], ndmin=5)
print("arr:\n", arr)
print("number of dimensions:", arr.ndim)