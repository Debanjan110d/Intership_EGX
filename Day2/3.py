import numpy as np


y = np.array([[1,2,3],[4,5,6]])
print(y.ndim) # 2 dimensional array

z = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(z[1,0,1:3])

x = np.array([1,2,3,4,5,9,8,55,66,77,88,99,100])
print(x[1:3])

print(x[-3:])

#LArgest
largest = 0
for item in x:
    if item > largest:
        largest = item
print(largest)

#Repeat

x = np.array([1,2,3,1,2,3,4,5,9,8,55,66,77,88,99,55,100,55])

diary = {}
for item in x:
    if item in diary:
        diary[item] += 1
    else:
        diary[item] = 1

for key, value in diary.items():
    if value > 1:
        print(f"{key}:{value} ")
print(diary)
