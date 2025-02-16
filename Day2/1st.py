import numpy as np 

np_array = np.array(10) # 0 Dimension Array
print(np_array.ndim)# ndim = number of dimensions

x = np.array([1,2,3,4,5])
print(x.ndim)# 1 dimensional array

y = np.array([[1,2,3],[4,5,6]])
print(y.ndim) # 2 dimensional array

z = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(z.ndim)# 3 dimensional array

non_structrual_3d_array = np.array([[[1,2,3]]])
print(non_structrual_3d_array.ndim) # 3 dimensional 

print(f"Type of np_array is {type(np_array)}")

# To create n-dimensional array
n = int(input("Enter the number of dimensions: "))
n_dim_array = np.array([[[[[[[1]]]]]]])
n_dim_array = n_dim_array.reshape(*([1]*n))
print(n_dim_array.ndim)

#Other Simple way to do it
take = int(input("Enter the number of dimensions: "))
n1_dim_array = np.array([1,2,3],ndmin=take)
print(n1_dim_array.ndim)

# ARray Indexing

print(y[1,2])
print(z[0,1,1])
