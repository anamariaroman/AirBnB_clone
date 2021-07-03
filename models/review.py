#!/usr/bin/python3
""" Defines a Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class that inherits from BaseModel
    And created public class attributes. """

    place_id = ""
    user_id = ""
    text = ""
