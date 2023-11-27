import json
import sqlite3
import time

import requests


def get_weather_data_for_location(latitude, longitude):
    """
    Get the average temperature for a location from the Open-Meteo API.

    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.
    
    Returns:
        float: The average temperature at 2pm for the given location.
    """
    # Define the Open-Meteo API endpoint
    api_url = "https://api.open-meteo.com/v1/forecast"

    # Set the coordinates
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "forecast_days": 7,
        "timesteps": "1:00:00",
        "hourly": "temperature_2m"
    }

    # Make the API request
    response = requests.get(api_url, params=params, timeout=5)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = json.loads(response.content)

        # Filter data for 2pm
        two_pm_data = []
        hourly_data = data["hourly"]
        for t, temperature in zip(hourly_data["time"], hourly_data["temperature_2m"]):
            if t.endswith("14:00"):
                two_pm_data.append(temperature)

        # Calculate the average temperature
        average_temperature_2pm = sum(two_pm_data) / len(two_pm_data)

        return average_temperature_2pm

    print("Error retrieving weather data")
    return None

# Read the district data from the JSON file
with open("data/bd-districts.json", "r", encoding="utf-8") as file:
    districts = json.load(file)["districts"]

    # Store the average temperatures for each district
    average_temperatures = []

    # Start the timer
    start = time.time()

    for district in districts:
        name = district["name"]
        lat = district["lat"]
        long = district["long"]

        average_temperatures.append(
            {
                "name": name,
                "average_temperature_2pm": get_weather_data_for_location(lat, long)
            }
        )

    # Sort the districts by average temperature
    top10_coolest_districts = sorted(average_temperatures,
                                     key=lambda x: x["average_temperature_2pm"])[:10]

    # Connect to the database
    conn = sqlite3.connect("data/weather.db")
    for item in top10_coolest_districts:
        # Insert the data into the database
        conn.execute("INSERT INTO weather (name, temperature) VALUES (?, ?)",
                     (item["name"], item["average_temperature_2pm"]))

    # Commit the changes
    conn.commit()
    conn.close()

    # count the time taken
    print(f"Time taken: {time.time() - start} seconds")
