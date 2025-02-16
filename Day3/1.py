import numpy as np

x = np.array([[1,2,3,4],[5,6,7,8]])
print(x.shape)

y =np.array([1,2,3,4])
print(y.shape)

# Reshape the 1D array to a 2D array of shape (2,2)
y =y.reshape(2,2)
print(y.shape)
