import numpy as np

# indexing in 1D array
arr_1d = np.array([0,1,2,3,4,5])
print('arr_1D:\n',arr_1d[2]) # arr[index]
print('arr_1D:\n',arr_1d[-1])

# indexing in 2D array
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('arr_2D:\n',arr_2d[1,2]) # arr[row(x) ,colum(y)]

# indexing in 3D array
arr_3 = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print('arr_3D:\n',arr_3)
print('arr_3D:\n',arr_3[0,1,2]) # arr[dimension(z), row(x), cloumn(y)]

# Boolean Indexing
arr = np.array([1,2,3,4,5,6,7])
mask = arr > 2
print('arr:\n',arr[mask])