""" Module for retrieving current device GPS coordinates by IP-address. """
from typing import NamedTuple
import geocoder


class Coordinates(NamedTuple):
    """ A named tuple for the coordinates of a location. """
    lat: float
    lng: float


def get_current_gps_coordinates() -> Coordinates:
    """
    Returns the current GPS coordinates of the device.
    :return: Tuple of latitude and longitude.
    """
    location = geocoder.ip('me')
    return Coordinates(location.lat, location.lng)


if __name__ == '__main__':
    coordinates = get_current_gps_coordinates()
    print(f"Latitude: {coordinates.lat}, Longitude: {coordinates.lng}")
