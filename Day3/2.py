import numpy as np

x =np.array([1,2,3,4])
y=np.array([5,6,7,8])
#Merging arrays
arr = np.concatenate((x,y))
print(arr)

#Splitting arrays
arr1,arr2 = np.split(arr,2)
print(arr1)
print(arr2)
#or
split_arr = np.array_split(arr,2)
print(split_arr)