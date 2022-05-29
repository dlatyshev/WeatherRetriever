from datetime import datetime
from pathlib import Path

from weather_api_service import Weather
from weather_formatter import format_weather


class WeatherStorage:
    """ Interface for any storage saving data. """

    def save(self, weather: Weather):
        raise NotImplementedError


class PlainFileWeatherStorage(WeatherStorage):
    """ Storage saving weather to a plain text file. """

    def __init__(self, path: Path):
        self.path = path

    def save(self, weather: Weather):
        with self.path.open('a+') as file:
            file.write("Date: {}\n".format(datetime.now()))
            file.write(format_weather(weather))
            file.write("\n________________________________________\n")




