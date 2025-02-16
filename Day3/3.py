import numpy as np

x = np.array([1,2,3,4,5])
# np.where() is a vectorized version of the if-else statement
# it takes three arguments: a condition, a value if the condition is true, and a value if the condition is false
# in this case, the condition is x > 3, the value if true is x, and the value if false is 0
# so the result is an array where all elements less than or equal to 3 are replaced with 0, and all elements greater than 3 are unchanged
y = np.where(x > 3, x, 0)
#or
# np.where() returns a tuple of arrays, one for each dimension of the input array
# the first element of the tuple is an array of indices where the condition is true
# the second element of the tuple is an array of columns where the condition is true
# since we are working with a 1D array, the column array is empty
# the [0][0] indexing extracts the first element of the first array, which is the index of the element equal to 4
index_of_4 = np.where(x == 4)[0][0]
print(index_of_4)


#sorting
x = np.array([100,28,13,14,95])
y = np.sort(x)
print(y)