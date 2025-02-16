import numpy as np
#Array Indexing

y = np.array([[1,2,3],[4,5,6]])
print(y.ndim) # 2 dimensional array

z = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(z.ndim)# 3 dimensional array

print(y[1,1])

print(z[1,0,2])