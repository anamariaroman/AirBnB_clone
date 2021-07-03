#!/usr/bin/python3
""" Defines a User class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class that inherits from BaseModel
    And created public class attributes. """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
