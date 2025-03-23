import pickle
import numpy as np

# Load the trained model
with open("crop_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load the label encoder
with open("label_encoder.pkl", "rb") as encoder_file:
    label_encoder = pickle.load(encoder_file)

# Function to get user input and make predictions
def predict_crop():
    print("\nEnter the following details to predict the best crop:")
    
    # Taking user input
    temperature = float(input("Temperature (°C): "))
    humidity = float(input("Humidity (%): "))
    water_availability = float(input("Water Availability: "))
    ph = float(input("Soil pH Level: "))

    # Creating input array
    input_data = np.array([[temperature, humidity, water_availability, ph]])
    
    # Predict the crop
    prediction = model.predict(input_data)
    
    # Convert numerical prediction to actual crop name
    predicted_crop = label_encoder.inverse_transform(prediction)[0]
    
    print(f"\n✅ Recommended Crop: {predicted_crop.upper()} 🌱")

# Call the function
predict_crop()
