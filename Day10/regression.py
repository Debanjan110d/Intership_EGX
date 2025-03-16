import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

# Load the CSV file into a DataFrame
df = pd.read_csv("Day10/Car.csv")

# fele dilam unnecessary columns: 'id', 'int_col', 'ext_col'
df.drop(['id', 'int_col', 'ext_col'], axis=1, inplace=True)

# Extract horsepower and engine displacement (liters) using regex
df[['horsepower', 'engine_liters']] = df['engine'].str.extract(r"(\d+\.?\d*)HP.*?(\d+\.\d+)L")

# float e kore nilam
df['horsepower'] = df['horsepower'].astype(float)
df['engine_liters'] = df['engine_liters'].astype(float)

# Drop the original 'engine' column as it's no longer needed
df.drop(['engine'], axis=1, inplace=True)

# ebar dekhlam t modified DataFrame
print(df.head())

# check korbo je horse power ar engine_liters e kono null valure ache ki na!
null_values = df[['horsepower', 'engine_liters']].isnull().sum()
print("Null values in horsepower and engine_liters:")
print(null_values)

# Fill missing values in 'engine_liters' with its mean
df['engine_liters'] = df['engine_liters'].fillna(df['engine_liters'].mean())

# Fill missing values in 'horsepower' with its mean
df['horsepower'] = df['horsepower'].fillna(df['horsepower'].mean())

# Display the modified DataFrame
print(df.head())

# ar null value nei
null_values = df[['horsepower', 'engine_liters']].isnull().sum()
print("Null values in horsepower and engine_liters:")
print(null_values)

# catagorical data alada kora
catagorical_data = ['brand', 'model', 'fuel_type', 'transmission', 'accident', 'clean_title']

encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
df[catagorical_data] = encoder.fit_transform(df[catagorical_data])

print(df.head())

y = df['price']
X = df.drop(['price'], axis=1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(X_scaled)

# Using a top-level regression model: XGBoost
model = XGBRegressor(n_estimators=200, learning_rate=0.1, max_depth=6, random_state=42)
model.fit(X_scaled, y)

# Make predictions
predictions = model.predict(X_scaled)

# Evaluate the model using Mean Squared Error
mse = mean_squared_error(y, predictions)
print(f"Mean Squared Error: {mse:.2f}")

# Plot the actual vs. predicted values
plt.scatter(y, predictions, alpha=0.5)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs. Predicted Values')
plt.show()

# Plot the residuals
residuals = y - predictions
plt.scatter(y, residuals, alpha=0.5)
plt.xlabel('Actual Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()

# Save the model
import joblib
joblib.dump(model, 'car_price_prediction_model.joblib')