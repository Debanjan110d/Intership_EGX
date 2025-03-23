# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns

# Load the dataset
df = pd.read_csv("Day11/crop.csv")

# Convert all text data to lowercase (if needed)
df = df.apply(lambda x: x.astype(str).str.lower() if x.dtype == "O" else x)

# Display first few rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)

# Check for duplicate rows
print(df.duplicated().sum())

#Fill null values
df['temperature'].fillna(df['temperature'].mean(), inplace=True)
df['humidity'].fillna(df['humidity'].mean(), inplace=True)
df['water availability'].fillna(df['water availability'].mean(), inplace=True)
df['ph'].fillna(df['ph'].mean(), inplace=True)


# Independent variables (features)
X = df[['temperature', 'humidity', 'water availability', 'ph']]

# Dependent variable (target)
y = df['label']  # We are predicting the crop type

# Encode target labels (if necessary)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)  # Convert crop names into numerical labels

# Splitting data into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Print classification report
print("Classification Report:\n", classification_report(y_test, y_pred))


# Example test data (Temperature, Humidity, Water Availability, pH)
test_data = [
    [25.0, 75.5, 220.0, 6.5],  # Example 1
    [30.2, 65.0, 180.3, 7.0],  # Example 2
    [20.5, 85.1, 250.2, 5.8],  # Example 3
    [27.8, 72.3, 200.4, 6.9]   # Example 4
]

# Convert test data to a DataFrame
test_df = pd.DataFrame(test_data, columns=['temperature', 'humidity', 'water availability', 'ph'])

# Make predictions using the trained model
predictions = model.predict(test_df)

# Convert numerical labels back to crop names
predicted_labels = label_encoder.inverse_transform(predictions)

# Display results
for i, pred in enumerate(predicted_labels):
    print(f"Test Case {i+1}: Predicted Crop -> {pred.upper()}")
