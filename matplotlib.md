## []: # matplotlib.md

# **Matplotlib: The Complete Guide (Beginner to Pro)**

## **1. Introduction to Matplotlib**

Matplotlib is a powerful Python library used for creating a wide variety of plots. It is widely used in data science, machine learning, and scientific computing.

### **Installation**

To install Matplotlib, use:

```bash
pip install matplotlib
```

Then, import it in Python:

```python
import matplotlib.pyplot as plt
```

---

## **2. Basic Plotting with Matplotlib**

### **2.1 Line Plot**

A simple line plot:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 18]

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.legend()
plt.grid(True)
plt.show()
```

**Explanation:**

-  `plot()` creates the plot.
-  `marker='o'` adds circular markers.
-  `linestyle='-'` sets the line style.
-  `color='b'` sets the color to blue.
-  `legend()` adds a label legend.
-  `grid(True)` enables the grid.

---

## **3. Customizing Plots**

Matplotlib allows extensive customization.

### **3.1 Changing Line Styles, Colors, and Markers**

```python
plt.plot(x, y, color='r', linestyle='--', marker='s', markersize=8, linewidth=2)
```

-  `color='r'` → Red line.
-  `linestyle='--'` → Dashed line.
-  `marker='s'` → Square markers.
-  `markersize=8` → Marker size.
-  `linewidth=2` → Line thickness.

### **3.2 Adding Labels, Titles, and Legends**

```python
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Line Plot')
plt.legend(['Data Line'])
plt.grid(True)
```

---

## **4. Different Types of Plots in Matplotlib**

Matplotlib supports various types of plots.

### **4.1 Scatter Plot**

Used for visualizing relationships between two variables.

```python
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='g', marker='x')
plt.xlabel('Random X')
plt.ylabel('Random Y')
plt.title('Scatter Plot')
plt.show()
```

### **4.2 Bar Plot**

Used for categorical data visualization.

```python
categories = ['A', 'B', 'C', 'D']
values = [20, 35, 30, 35]

plt.bar(categories, values, color=['red', 'blue', 'green', 'orange'])
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()
```

### **4.3 Histogram**

Used for frequency distribution.

```python
data = np.random.randn(1000)

plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()
```

### **4.4 Pie Chart**

Used for percentage representation.

```python
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 30, 15, 15]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['blue', 'red', 'green', 'yellow'])
plt.title('Programming Language Popularity')
plt.show()
```

### **4.5 Box Plot**

Used for statistical data representation.

```python
data = [np.random.randn(100), np.random.randn(100), np.random.randn(100)]

plt.boxplot(data, labels=['A', 'B', 'C'])
plt.title('Box Plot Example')
plt.show()
```

---

## **5. Subplots: Multiple Plots in One Figure**

Matplotlib allows multiple plots in a single figure.

### **5.1 Creating Subplots**

```python
fig, axs = plt.subplots(2, 2, figsize=(8, 8))

axs[0, 0].plot(x, y, 'r-')
axs[0, 0].set_title("Line Plot")

axs[0, 1].scatter(x, y, color='g')
axs[0, 1].set_title("Scatter Plot")

axs[1, 0].bar(categories, values, color='b')
axs[1, 0].set_title("Bar Chart")

axs[1, 1].hist(data, bins=20, color='purple')
axs[1, 1].set_title("Histogram")

plt.tight_layout()
plt.show()
```

-  `subplots(2, 2)` creates a 2x2 grid.
-  `axs[i, j]` selects individual plots.

---

## **6. Advanced Matplotlib Features**

### **6.1 3D Plotting**

```python
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title("3D Surface Plot")
plt.show()
```

### **6.2 Animated Plots**

```python
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.arange(0, 10, 0.1)
line, = ax.plot(x, np.sin(x))

def update(frame):
    line.set_ydata(np.sin(x + frame / 10))
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50)
plt.show()
```

---

## **7. Matplotlib with Pandas for Data Analysis**

Matplotlib integrates well with Pandas.

```python
import pandas as pd

data = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D'],
    'Value': [10, 20, 15, 25]
})

data.plot(kind='bar', x='Name', y='Value', color='green')
plt.title("Pandas Data Plot")
plt.show()
```

---

## **8. Saving Figures**

Matplotlib allows saving plots as images.

```python
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
```

-  `dpi=300` → High resolution.
-  `bbox_inches='tight'` → Removes unnecessary white space.

---

## **9. Interactive Plots with `plt.show(block=False)`**

```python
plt.plot(x, y)
plt.show(block=False)
input("Press Enter to close the plot...")
```

This keeps the plot interactive without stopping execution.

---

## **10. Summary of Matplotlib**

| Feature             | Description                           |
| ------------------- | ------------------------------------- |
| Line Plot           | `plt.plot()` for continuous data      |
| Scatter Plot        | `plt.scatter()` for relationships     |
| Bar Chart           | `plt.bar()` for categorical data      |
| Histogram           | `plt.hist()` for distribution         |
| Pie Chart           | `plt.pie()` for percentages           |
| Box Plot            | `plt.boxplot()` for statistics        |
| 3D Plot             | `plot_surface()` for 3D visualization |
| Animations          | `FuncAnimation()` for animated plots  |
| Subplots            | `plt.subplots()` for multiple plots   |
| Pandas & Matplotlib | `df.plot()` for data analysis         |
| Saving Figures      | `plt.savefig()` for exporting plots   |

---

## **Conclusion**

Matplotlib is a powerful library for data visualization. It provides flexibility, customization, and integrates well with NumPy, Pandas, and SciPy. With practice, you can create professional-grade visualizations for data analysis, machine learning, and reporting.

---
