#!/usr/bin/python3
"""Module defining the Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class that represents an amenity.

    Public class attributes:
        name (str): The name of the amenity.
    """
    name = ""
