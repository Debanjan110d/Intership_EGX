import pickle
import numpy as np
from django.shortcuts import render
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    """Render the home page with the input form"""
    return render(request, 'predictor/index.html')

def predict(request):
    """Process the form data and make prediction"""
    if request.method == 'POST':
        # Get data from form
        temperature = float(request.POST.get('temperature'))
        humidity = float(request.POST.get('humidity'))
        water_availability = float(request.POST.get('water_availability'))
        ph = float(request.POST.get('ph'))
        
        # Load model and encoder
        model_path = os.path.join(BASE_DIR, 'crop_model.pkl')
        encoder_path = os.path.join(BASE_DIR, 'label_encoder.pkl')
        
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file) 
            
        with open(encoder_path, 'rb') as encoder_file:
            label_encoder = pickle.load(encoder_file)
        
        # Make prediction
        input_data = np.array([[temperature, humidity, water_availability, ph]])
        prediction = model.predict(input_data)
        predicted_crop = label_encoder.inverse_transform(prediction)[0]
        
        # Pass result to template
        context = {
            'crop': predicted_crop.upper(),
            'temperature': temperature,
            'humidity': humidity,
            'water_availability': water_availability,
            'ph': ph
        }
        
        return render(request, 'predictor/result.html', context)
    
    # If not POST, redirect to home page
    return render(request, 'predictor/index.html')