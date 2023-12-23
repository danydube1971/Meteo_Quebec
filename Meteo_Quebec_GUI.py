import requests
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Function to fetch weather data
def fetch_weather():
    api_key = "7f7a446f0033fa4829f734ac2088890e"
    lat = 46.8138783
    lon = -71.2079809
    units = "metric"
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}&lang=fr"

    response = requests.get(url)
    if response.status_code != 200:
        weather_display.config(text="Erreur : Impossible de récupérer les données météo.")
        return

    data = response.json()
    display_weather(data)

# Function to load and return an image based on weather description
def get_weather_image(description):
    if "couvert" in description:
        image_path = resource_path("couvert.jpg")
    elif "nuageux" in description:
        image_path = resource_path("nuageux.jpg")
    elif "ensoleillé" in description:
        image_path = resource_path("soleil.jpg")
    elif "pluie" in description:
        image_path = resource_path("pluie.jpg")
    elif "légère pluie" in description:
        image_path = resource_path("legere_pluie.jpg")
    elif "neige" in description:
        image_path = resource_path("neige.jpg")
    else:
        image_path = resource_path("default.jpg") # Default image if no match found

    # Load and return the image
    image = Image.open(image_path)
    image = image.resize((100, 100), Image.Resampling.LANCZOS)  # Resize if necessary
    return ImageTk.PhotoImage(image)

# Function to display weather data
def display_weather(data):
    chosen_date_str = date_selection.get_date()
    chosen_date = datetime.strptime(chosen_date_str, '%Y-%m-%d').date()  # Convert string to datetime.date object

    closest_forecast = None
    closest_time_diff = float('inf')
    for forecast in data['list']:
        forecast_date = datetime.fromtimestamp(forecast['dt']).date()  # Get only the date part
        time_diff = (forecast_date - chosen_date).total_seconds()
        if time_diff >= 0 and time_diff < closest_time_diff:
            closest_forecast = forecast
            closest_time_diff = time_diff

    if closest_forecast:
        forecast_datetime = datetime.fromtimestamp(closest_forecast['dt'])
        temp = closest_forecast['main']['temp']
        description = closest_forecast['weather'][0]['description']
        precipitation = closest_forecast.get('rain', {}).get('3h', 0)  # Get precipitation in mm, default to 0 if not present

        weather_display.config(text=f"Date: {forecast_datetime.strftime('%Y-%m-%d %H:%M')}\nTempérature: {temp}°C\nDescription: {description}\nPrécipitations: {precipitation} mm")
        
        # Load and display the weather image
        weather_image = get_weather_image(description)
        image_label.config(image=weather_image)
        image_label.image = weather_image  # Keep a reference
    else:
        weather_display.config(text="Aucune donnée disponible pour cette date.")
        image_label.config(image='')

# GUI setup
root = tk.Tk()
root.title("Météo Québec v.2.0")

# Date selection
date_selection = Calendar(root)
date_selection.pack(pady=10)

# Fetch weather button
fetch_button = tk.Button(root, text="Obtenir la météo", command=fetch_weather)
fetch_button.pack(pady=10)

# Weather display
weather_display = tk.Label(root, text="Veuillez choisir une date et cliquer sur 'Obtenir la météo'.")
weather_display.pack(pady=10)

# Label for weather image
image_label = tk.Label(root)
image_label.pack(pady=10)

root.mainloop()

