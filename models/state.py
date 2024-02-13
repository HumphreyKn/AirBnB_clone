#!/usr/bin/python3
"""Module defining the State class."""

from models.base_model import BaseModel


class State(BaseModel):
    """A class that represents a State.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
