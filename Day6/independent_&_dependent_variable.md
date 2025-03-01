### **Independent and Dependent Variables in Machine Learning**

In machine learning, understanding **independent** and **dependent** variables is crucial because they define how a model learns and makes predictions.

---

## **1. Independent Variables (Features)**

-  These are **input** variables that influence the output.
-  They are also called **predictors**, **features**, or **explanatory variables**.
-  In supervised learning, we provide these variables as input to train the model.

#### **Example:**

If we are predicting house prices based on square footage and number of bedrooms:

-  **Independent Variables (Features):** Square footage, Number of bedrooms

---

## **2. Dependent Variable (Target)**

-  This is the **output** variable the model is trying to predict.
-  It depends on the independent variables.
-  Also called **response variable**, **target variable**, or **label**.

#### **Example (Continued):**

-  **Dependent Variable (Target):** House price

---

### **Real-Life Examples**

| **Scenario**              | **Independent Variable (Features)**           | **Dependent Variable (Target)** |
| ------------------------- | --------------------------------------------- | ------------------------------- |
| Predicting house prices   | Square footage, No. of bedrooms, Location     | House Price                     |
| Predicting student grades | Study hours, Attendance, Past scores          | Exam Score                      |
| Weather prediction        | Temperature, Humidity, Wind speed             | Rainfall (Yes/No)               |
| Stock price prediction    | Trading volume, Market trends, News Sentiment | Stock Price                     |

---

## **3. Code Explanation Using Python**

Let's implement a simple **Linear Regression** model where we predict a student's exam score based on the number of hours studied.

### **Step 1: Import Libraries**

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
```

### **Step 2: Create Sample Data**

```python
# Independent variable (Hours Studied)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)

# Dependent variable (Exam Score)
y = np.array([40, 50, 55, 65, 70, 75, 78, 85, 90, 95])
```

Here:

-  `X` is the **independent variable** (hours studied).
-  `y` is the **dependent variable** (exam score).

### **Step 3: Split Data into Train & Test Sets**

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

-  80% data is used for training.
-  20% data is used for testing.

### **Step 4: Train the Model**

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

The model learns the relationship between **hours studied** and **exam score**.

### **Step 5: Make Predictions**

```python
y_pred = model.predict(X_test)
```

### **Step 6: Evaluate Model Performance**

```python
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"R² Score: {r2}")
```

-  **Mean Absolute Error (MAE):** Measures how far predictions are from actual values.
-  **R² Score:** Measures how well the independent variable explains the dependent variable.

### **Step 7: Visualizing the Model**

```python
plt.scatter(X_train, y_train, color='blue', label="Training Data")
plt.scatter(X_test, y_test, color='red', label="Test Data")
plt.plot(X, model.predict(X), color='green', linestyle='dashed', label="Regression Line")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.legend()
plt.title("Linear Regression: Hours Studied vs Exam Score")
plt.show()
```

---

## **4. Key Takeaways**

✅ **Independent Variable** → Input that affects the outcome (Features)  
✅ **Dependent Variable** → The result we predict (Target)  
✅ **Machine Learning models** find relationships between independent and dependent variables.  
✅ **Linear Regression Example**: Predicting exam scores using study hours.

---

## **5. Additional Resources**

-  [Machine Learning Guide](https://machinelearningmastery.com/what-is-machine-learning/)
-  [Linear Regression Example](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html#sphx-glr-auto-examples-linear-model-plot-ols-py)
