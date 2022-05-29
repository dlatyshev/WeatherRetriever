import geocoder
from typing import NamedTuple


class Coordinates(NamedTuple):
    lat: float
    lng: float


def get_current_gps_coordinates() -> Coordinates:
    """
    Returns the current GPS coordinates of the device.
    :return: Tuple of latitude and longitude.
    """
    g = geocoder.ip('me')
    return Coordinates(g.lat, g.lng)


if __name__ == '__main__':
    coordinates = get_current_gps_coordinates()
    print(f"Latitude: {coordinates.lat}, Longitude: {coordinates.lng}")