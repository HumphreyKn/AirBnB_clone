#!/usr/bin/python3
"""Module defining the Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class that represents a review.

    Public class attributes:
        place_id (str): The place ID associated with the review (Place.id).
        user_id (str): The user ID associated with the review (User.id).
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ''
    text = ''
