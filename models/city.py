#!/usr/bin/python3
""" Defines a City class """
from models.base_model import BaseModel


class City(BaseModel):
    """ Class that inherits from BaseModel
    And created public class attributes. """

    state_id = ""
    name = ""
