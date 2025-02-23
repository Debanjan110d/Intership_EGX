import matplotlib.pyplot as plt
import numpy as np

x = np.array([10,20,30,40,50,60,70,80,90,100])
y = np.array([15, 7, 19, 11, 13, 16, 12, 18, 14, 20])
z = np.array([1,2,3,4,5,6,7,8,9,10])

# Create a scatter plot
plt.scatter(x,y)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Scatter Plot')

plt.show()

# Create a line plot
plt.plot(x,y)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Plot')

plt.show()

# Create a bar chart
plt.bar(x,y)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Bar Chart')

plt.show()

# Create a histogram
plt.hist(x)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Histogram')

plt.show()

# Create a pie chart
plt.pie(x)

plt.title('Pie Chart')

plt.show()

# Create a box plot
plt.boxplot(x)

plt.title('Box Plot')

plt.show()

# Create a violin plot
plt.violinplot(x)

plt.title('Violin Plot')

plt.show()

# Create a heatmap
plt.imshow([x])

plt.title('Heatmap')

plt.show()

# Create a contour plot
plt.contour([x], [y])

plt.title('Contour Plot')

plt.show()

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Scatter Plot')

plt.show()

# Create a 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Surface Plot')

plt.show()

# Create a 3D bar chart
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.bar3d(x,y,z,1,1,1)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Bar Chart')

plt.show()

# Create a 3D line plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Line Plot')

plt.show()

