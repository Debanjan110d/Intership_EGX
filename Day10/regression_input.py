import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

# Load the CSV file into a DataFrame
df = pd.read_csv("Day10/Car.csv")

# Remove unnecessary columns
df.drop(['id', 'int_col', 'ext_col'], axis=1, inplace=True)

# Extract numerical values from the 'engine' column
df[['horsepower', 'engine_liters']] = df['engine'].str.extract(r"(\d+\.?\d*)HP.*?(\d+\.\d+)L")

# Convert to float
df['horsepower'] = df['horsepower'].astype(float)
df['engine_liters'] = df['engine_liters'].astype(float)

# Drop the original 'engine' column
df.drop(['engine'], axis=1, inplace=True)

# Check for null values
null_values = df[['horsepower', 'engine_liters']].isnull().sum()
print("Null values in horsepower and engine_liters:")
print(null_values)

# Fill missing values with the mean
df['engine_liters'].fillna(df['engine_liters'].mean(), inplace=True)
df['horsepower'].fillna(df['horsepower'].mean(), inplace=True)

# Encode categorical data
categorical_columns = ['brand', 'model', 'fuel_type', 'transmission', 'accident', 'clean_title']
encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
df[categorical_columns] = encoder.fit_transform(df[categorical_columns])

# Define target variable and features
y = df['price']
X = df.drop(['price'], axis=1)

# Scale the numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train an XGBoost regression model
model = XGBRegressor(n_estimators=200, learning_rate=0.1, max_depth=6, random_state=42)
model.fit(X_scaled, y)

# Make predictions
predictions = model.predict(X_scaled)

# Evaluate the model
mse = mean_squared_error(y, predictions)
print(f"Mean Squared Error: {mse:.2f}")

# Plot actual vs predicted values
plt.scatter(y, predictions, alpha=0.5)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs. Predicted Values')
plt.show()

# Plot residuals
residuals = y - predictions
plt.scatter(y, residuals, alpha=0.5)
plt.xlabel('Actual Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()
