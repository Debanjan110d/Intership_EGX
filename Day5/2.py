import matplotlib.pyplot as plt
import numpy as np

x_axis = np.array(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
y_axis = np.array([12000, 11000, 13000, 12500, 12000, 11500, 14000, 13500, 12500, 13000, 14500, 14000])

# Done by me 

# plt.bar(x_axis, y_axis)
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.title("Sales per month")
# plt.show()

#Done by sir 

# plt.plot(x_axis, y_axis)
# plt .show()

#2 done by sir


# Create a bar chart with x_axis as months and y_axis as sales
plt.bar(x_axis, y_axis)

# Label the x-axis as "Months"
plt.xlabel("Months")

# Label the y-axis as "Sales"
plt.ylabel("Sales")

# Set the title of the plot to "Sales per month"
plt.title("Sales per month")

# Set the x-ticks to be the months from x_axis
plt.xticks(x_axis)

# Add a grid to the plot for better readability
plt.grid()

# Display the plot
plt.show()

