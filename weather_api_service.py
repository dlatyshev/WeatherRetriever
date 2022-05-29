""" Module for retrieving weather data by coordinates. """
import os
from typing import NamedTuple
from datetime import datetime
from enum import Enum
import requests


Celsius = float
Percents = float
URL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}&units=metric"


class WeatherType(Enum):
    """ Represents the weather type. """

    THUNDERSTORM = "Thunderstorm"
    DRIZZLE = "Drizzle"
    RAIN = "Rain"
    SNOW = "Snow"
    CLEAR = "Clear"
    CLOUDS = "Clouds"
    FOG = "Fog"
    DUST = "Dust"


class Weather(NamedTuple):
    """ A named tuple for the weather data. """
    temperature: Celsius
    feels_like: Celsius
    weather_type: WeatherType
    humidity: Percents
    pressure: float
    city: str
    country: str
    sunrise: datetime
    sunset: datetime


def get_current_weather_by_coordinates(lat, lng) -> Weather:
    """
    Returns the current weather at the given coordinates.
    :return Weather: The current weather.
    """
    api_key = os.environ['WEATHER_API_KEY']
    data = requests.get(URL.format(lat=lat, lng=lng, api_key=api_key)).json()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    weather_type = WeatherType(data['weather'][0]['main'])
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    city = data['name']
    country = data['sys']['country']
    sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
    sunset = datetime.fromtimestamp(data['sys']['sunset'])
    return Weather(temp, feels_like, weather_type, humidity, pressure, city, country, sunrise, sunset)
