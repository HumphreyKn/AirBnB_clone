#!/usr/bin/python3
"""Module defining the Place class."""

from models.base_model import BaseModel


class Place(BaseModel):
    """A class that represents a place.

    Public class attributes:
        city_id (str): The city ID associated with the place (City.id).
        user_id (str): The user ID associated with the place (User.id).
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The max number of guests the place can accommodate.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): List amenityIDs associatd with place (Amenity.id)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []
