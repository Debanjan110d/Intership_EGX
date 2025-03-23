import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("Day11/crop.csv")

# Define independent (X) and dependent (y) variables
X = df[['temperature', 'humidity', 'water availability', 'ph']]  # Features
y = df['label']  # Target

# Encode the crop labels (categorical to numerical)
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)  # Convert crop names to numbers

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and label encoder using pickle
with open("crop_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)
    
with open("label_encoder.pkl", "wb") as encoder_file:
    pickle.dump(label_encoder, encoder_file)

print("Model saved successfully!")
