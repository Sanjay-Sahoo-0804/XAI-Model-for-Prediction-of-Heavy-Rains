# import streamlit as st
# import requests
# from datetime import datetime

# # API key and list of cities
# API_KEY = '2e0dd887d68875346b419190ffa358ed'
# cities = sorted(['Amaravathi', 'Guntur', 'Machilipatnam', 'Mangalagiri', 'Nandigama', 'Tenali', 'Vijayawada'])

# # Sidebar selection for city
# CITY = f"{st.sidebar.selectbox('Select a city in the Vijayawada area', cities)}, IN"

# # CSS for styling
# st.markdown("""
#     <style>
#     /* Background Image */
#     body {
#         background-image: url('https://your-image-url.com'); /* Add your image URL here */
#         background-size: cover;
#         background-position: center;
#         color: #ffffff;
#     }

#     /* Sidebar Styling */
#     .sidebar .sidebar-content {
#         background-color: #e74c3c; /* Change to red */
#     }
#     .sidebar .sidebar-header {
#         background-color: #c0392b; /* Change to dark red */
#         color: white;
#     }
#     .sidebar .sidebar-item {
#         color: #ecf0f1;
#     }
#     .sidebar .sidebar-item:hover {
#         background-color: #e74c3c; /* Hover effect */
#         color: white;
#     }

#     /* Title Styling */
#     h1 {
#         color: #1abc9c;
#         font-size: 2.5rem;
#         font-family: 'Arial', sans-serif;
#         font-weight: bold;
#     }

#     /* Weather Cards Styling */
#     .weather-card {
#         background-color: rgba(0, 0, 0, 0.6);
#         padding: 20px;
#         margin-bottom: 20px;
#         border-radius: 10px;
#         color: white;
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         font-family: 'Arial', sans-serif;
#     }

#     /* Weather Icon Styling */
#     .weather-icon {
#         width: 50px;
#         height: 50px;
#     }

#     /* Section Headers */
#     .section-header {
#         color: #1abc9c;
#         font-size: 1.5rem;
#         font-weight: bold;
#     }

#     /* Farm Friendly Explanation */
#     .farm-note {
#         background-color: #34495e;
#         padding: 10px;
#         border-radius: 5px;
#         color: white;
#         font-size: 1.1rem;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Title
# st.title("RainReady")

# # Icon mapping for weather
# icon_mapping = {
#     'Rain': 'https://img.icons8.com/ios-filled/50/ffffff/rain.png',
#     'Clear': 'https://img.icons8.com/ios-filled/50/ffffff/sun.png',
#     'Clouds': 'https://img.icons8.com/ios-filled/50/ffffff/cloud.png',
# }

# # Function to fetch weather data
# def fetch_weather_data(api_key, city):
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         st.error(f"Error: Could not fetch data for {city}. Status code {response.status_code}")
#         return None

# # Farm-friendly explanation function
# def generate_farm_friendly_explanation(temp_min, temp_max, humidity, wind_speed, prediction):
#     explanation = f"Weather Prediction: {prediction}\n\n"

#     # Humidity Explanation
#     if humidity > 85:
#         explanation += f"High humidity ({humidity}%). Rain likely. Farmers should ensure field drainage."
#     elif 65 <= humidity <= 85:
#         explanation += f"Moderate humidity ({humidity}%), beneficial rain likely."
#     elif 45 <= humidity < 65:
#         explanation += f"Moderate humidity ({humidity}%), light rain may occur."
#     else:
#         explanation += f"Low humidity ({humidity}%). Rain unlikely, consider irrigation."

#     # Min Temperature Explanation
#     if temp_min < 10:
#         explanation += f"\n\nLow temp ({temp_min}°C) might risk frost for sensitive crops."
#     elif 10 <= temp_min <= 20:
#         explanation += f"\n\nModerate low temp ({temp_min}°C), stable conditions expected."
#     else:
#         explanation += f"\n\nWarmer low temp ({temp_min}°C), limited dew, soil may dry."

#     # Max Temperature Explanation
#     if temp_max < 20:
#         explanation += f"\n\nCool max temp ({temp_max}°C), gentle rain likely."
#     elif 20 <= temp_max <= 30:
#         explanation += f"\n\nModerate max temp ({temp_max}°C), steady rain, should dry quickly."
#     else:
#         explanation += f"\n\nHigh max temp ({temp_max}°C), intense rain possible."

#     # Wind Speed Explanation
#     if wind_speed < 5:
#         explanation += f"\n\nLow wind speed ({wind_speed} km/h), rain likely to fall steadily."
#     elif 5 <= wind_speed <= 15:
#         explanation += f"\n\nModerate wind speed ({wind_speed} km/h), steady rain without extreme gusts."
#     else:
#         explanation += f"\n\nHigh wind speed ({wind_speed} km/h), possible heavy rain with gusts."

#     return explanation

# # Fetch weather data
# weather_data = fetch_weather_data(API_KEY, CITY)

# # Display forecast data if available
# if weather_data and 'list' in weather_data:
#     st.write(f'Weather forecast for the next 7 days in {CITY}:')
    
#     # Group forecast data by date
#     daily_data = {}
#     for forecast in weather_data['list']:
#         forecast_datetime = datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S')
#         date_str = forecast_datetime.strftime('%Y-%m-%d')
#         if date_str not in daily_data:
#             daily_data[date_str] = []
#         daily_data[date_str].append(forecast)

#     # User selects a date to view hourly forecasts
#     selected_date = st.selectbox("Select a date to view hourly predictions", list(daily_data.keys())[:7])

#     # Display each 3-hour forecast for the selected date
#     st.write(f"Hourly predictions for {selected_date}:")
#     for forecast in daily_data[selected_date]:
#         hourly_datetime = datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S')
#         temp_min = forecast['main']['temp_min']
#         temp_max = forecast['main']['temp_max']
#         humidity = forecast['main']['humidity']
#         windspeed = forecast['wind']['speed']
#         weather_description = forecast['weather'][0]['main']  # Short description like "Rain" or "Clear"

#         # Get icon based on weather description
#         icon_url = icon_mapping.get(weather_description, 'https://img.icons8.com/ios-filled/50/ffffff/question-mark.png')

#         # Generate farm-friendly explanation
#         farm_explanation = generate_farm_friendly_explanation(temp_min, temp_max, humidity, windspeed, weather_description)

#         # Display each hourly forecast in a styled card
#         st.markdown(f"""
#             <div class="weather-card">
#                 <div>
#                     <strong>Time: {hourly_datetime.strftime('%H:%M:%S')}</strong><br>
#                     Temp Min: {temp_min}°C<br>
#                     Temp Max: {temp_max}°C<br>
#                     Humidity: {humidity}%<br>
#                     Wind Speed: {windspeed} km/h<br>
#                     Prediction: {weather_description}<br><br>
#                     <strong>Farmer's Note:</strong><br>
#                     <div class="farm-note">{farm_explanation}</div>
#                 </div>
#                 <div>
#                     <img src="{icon_url}" class="weather-icon">
#                 </div>
#             </div>
#         """, unsafe_allow_html=True)
# else:
#     st.write('Error fetching weather data. Please check your API key and city name.')
import streamlit as st
import requests
import joblib
import numpy as np
import pandas as pd
from datetime import datetime

# Load the trained model
MODEL_PATH = "data/rainfall_model.pkl"
model = joblib.load(MODEL_PATH)

# API key and list of cities
API_KEY = "2e0dd887d68875346b419190ffa358ed"
cities = sorted(['Amaravathi', 'Guntur', 'Machilipatnam', 'Mangalagiri', 'Nandigama', 'Tenali', 'Vijayawada'])

# Sidebar selection for city
CITY = f"{st.sidebar.selectbox('Select a city in the Vijayawada area', cities)}, IN"

# CSS for styling
st.markdown("""
    <style>
    /* General Page Styling */
    body {
        background-color: #f7f7f7;
        font-family: Arial, sans-serif;
    }
    
    /* Title Styling */
    h1 {
        color: #2c3e50;
        text-align: center;
    }

    /* Weather Card Styling */
    .weather-card {
        background-color: #ecf0f1;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    /* Prediction Styling */
    .prediction-box {
        background-color: #3498db;
        padding: 10px;
        border-radius: 5px;
        color: white;
        text-align: center;
        font-size: 1.2rem;
    }

    /* Weather Icon Styling */
    .weather-icon {
        width: 50px;
        height: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("RainReady - Rainfall Prediction")

# Function to fetch weather data
def fetch_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: Could not fetch data for {city}. Status code {response.status_code}")
        return None

# Function to predict rainfall using the model
def predict_rainfall(features):
    features = np.array(features).reshape(1, -1)  # Reshape for model input
    prediction = model.predict(features)[0]
    return "Rain Expected" if prediction == 1 else "No Rain"

# Fetch weather data
weather_data = fetch_weather_data(API_KEY, CITY)

# Display forecast data and predictions
if weather_data and 'list' in weather_data:
    st.write(f'Weather forecast for the next 5 days in {CITY}:')

    # Process daily weather data
    daily_data = {}
    for forecast in weather_data['list']:
        date_str = forecast['dt_txt'].split(" ")[0]  # Extract date
        if date_str not in daily_data:
            daily_data[date_str] = []
        daily_data[date_str].append(forecast)

    # User selects a date to view predictions
    selected_date = st.selectbox("Select a date", list(daily_data.keys())[:5])

    # Display prediction for the selected date
    st.write(f"Rainfall Prediction for {selected_date}:")

    for forecast in daily_data[selected_date]:
        time_str = forecast['dt_txt'].split(" ")[1]
        temp = forecast['main']['temp']
        humidity = forecast['main']['humidity']
        pressure = forecast['main']['pressure']
        wind_speed = forecast['wind']['speed']
        weather_desc = forecast['weather'][0]['main']

        # Prepare features for prediction
        features = [temp, humidity, pressure, wind_speed]
        rainfall_prediction = predict_rainfall(features)

        # Weather card
        st.markdown(f"""
            <div class="weather-card">
                <div>
                    <strong>Time: {time_str}</strong><br>
                    Temp: {temp}°C<br>
                    Humidity: {humidity}%<br>
                    Pressure: {pressure} hPa<br>
                    Wind Speed: {wind_speed} km/h<br>
                    Weather: {weather_desc}<br>
                </div>
                <div class="prediction-box">{rainfall_prediction}</div>
            </div>
        """, unsafe_allow_html=True)
else:
    st.write('Error fetching weather data. Please check your API key and city name.')
