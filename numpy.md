NumPy (Numerical Python) is a powerful Python library for **numerical computing**. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

---

# **🚀 NumPy Uses & Features**

## **1. Installing & Importing NumPy**

```python
pip install numpy  # Install NumPy
import numpy as np  # Import NumPy
```

---

## **2. Creating NumPy Arrays**

-  **1D array (Vector)**
   ```python
   arr = np.array([1, 2, 3, 4])
   print(arr)
   ```
-  **2D array (Matrix)**
   ```python
   arr2d = np.array([[1, 2], [3, 4]])
   print(arr2d)
   ```
-  **3D array (Tensor)**
   ```python
   arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
   ```

---

## **3. Checking Array Properties**

```python
print(arr.shape)   # (Rows, Columns)
print(arr.size)    # Total elements
print(arr.ndim)    # Number of dimensions
print(arr.dtype)   # Data type (int, float, etc.)
```

---

## **4. Creating Special Arrays**

-  **Array of zeros**
   ```python
   np.zeros((3, 3))
   ```
-  **Array of ones**
   ```python
   np.ones((2, 2))
   ```
-  **Identity matrix**
   ```python
   np.eye(3)  # 3x3 identity matrix
   ```
-  **Random numbers**
   ```python
   np.random.rand(3, 3)  # Uniform distribution
   np.random.randn(3, 3)  # Standard normal distribution
   np.random.randint(1, 10, (2, 3))  # Random integers
   ```
-  **Evenly spaced numbers**
   ```python
   np.linspace(1, 10, 5)  # 5 numbers between 1 and 10
   np.arange(1, 10, 2)  # Numbers from 1 to 9 with step 2
   ```

---

## **5. Indexing & Slicing**

```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[2])  # Access element at index 2 → 30
print(arr[:3])  # First 3 elements → [10, 20, 30]
print(arr[-1])  # Last element → 50
```

-  **2D Array Indexing**
   ```python
   arr2d = np.array([[1, 2, 3], [4, 5, 6]])
   print(arr2d[1, 2])  # Row 1, Column 2 → 6
   print(arr2d[:, 1])  # All rows, Column 1 → [2, 5]
   ```

---

## **6. Mathematical Operations**

```python
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)  # Element-wise addition → [5, 7, 9]
print(arr1 * arr2)  # Element-wise multiplication → [4, 10, 18]
print(arr1 ** 2)    # Squaring each element → [1, 4, 9]
print(np.exp(arr1))  # Exponential function
print(np.sqrt(arr1))  # Square root
print(np.log(arr1))  # Natural logarithm
```

---

## **7. Aggregate Functions**

```python
arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))   # Sum → 15
print(np.mean(arr))  # Mean → 3.0
print(np.min(arr))   # Minimum → 1
print(np.max(arr))   # Maximum → 5
print(np.std(arr))   # Standard deviation
print(np.var(arr))   # Variance
```

---

## **8. Matrix Operations**

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.dot(A, B))  # Matrix multiplication
print(A @ B)  # Alternative for matrix multiplication
print(np.linalg.inv(A))  # Inverse of a matrix
print(np.linalg.det(A))  # Determinant
print(np.transpose(A))  # Transpose of a matrix
```

---

## **9. Reshaping & Flattening**

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.reshape(3, 2))  # Reshape into 3 rows, 2 columns
print(arr.flatten())  # Convert to 1D array
```

---

## **10. Stacking & Splitting Arrays**

-  **Stacking arrays**
   ```python
   np.hstack([arr1, arr2])  # Horizontal stacking
   np.vstack([arr1, arr2])  # Vertical stacking
   ```
-  **Splitting arrays**
   ```python
   np.hsplit(arr, 2)  # Split into 2 horizontal parts
   np.vsplit(arr, 2)  # Split into 2 vertical parts
   ```

---

## **11. Boolean Indexing & Filtering**

```python
arr = np.array([10, 20, 30, 40])

print(arr[arr > 20])  # [30, 40]
print(np.where(arr > 20, "High", "Low"))  # ['Low' 'Low' 'High' 'High']
```

---

## **12. Broadcasting (Operations on Different Shapes)**

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr + 10)  # Adds 10 to each element
```

---

## **13. Reading & Writing Files**

```python
np.savetxt("array.txt", arr, delimiter=",")  # Save to file
np.loadtxt("array.txt", delimiter=",")  # Load from file
```

---

## **14. Working with NaN Values**

```python
arr = np.array([1, 2, np.nan, 4, 5])

print(np.isnan(arr))  # [False False  True False False]
print(np.nanmean(arr))  # Mean ignoring NaN
```

---

## **15. NumPy & Pandas Together**

```python
import pandas as pd

data = np.random.rand(5, 3)  # 5 rows, 3 columns
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)
```

---

### **🚀 Summary**

NumPy is **essential** for scientific computing, data analysis, and machine learning. It provides **fast numerical operations, efficient memory handling, and seamless integration with libraries like pandas, Matplotlib, and TensorFlow**.
