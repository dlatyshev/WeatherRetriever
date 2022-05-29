""" Module for formatting weather data. """
from weather_api_service import Weather


def format_weather(weather_data: Weather) -> str:
    """
    Returns a formatted string of the weather data.
    """
    return f"""
    Current weather in {weather_data.city}, {weather_data.country}:
    Temperature: {weather_data.temperature} °C
    Feels like: {weather_data.feels_like} °C
    Weather type: {weather_data.weather_type}
    Humidity: {weather_data.humidity} %
    Pressure: {weather_data.pressure} hPa
    Sunrise: {weather_data.sunrise}
    Sunset: {weather_data.sunset}
    """
