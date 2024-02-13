#!/usr/bin/python3
"""Module defining the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """A class that represents a City.

    Attributes:
        name (str): The name of the City.
        state_id (str): it will be the State.id
    """
    state_id = ""
    name = ""
