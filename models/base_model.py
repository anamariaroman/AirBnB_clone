#!/usr/bin/python3
""" Base class """
from uuid import uuid4
from datetime import datetime
import json


class BaseModel:
    """ Base class model that contains the all methods and attributes for the some classes """

    def __init__(self, *args, **kwargs):
        """ Constructor to initialize the attribute with args and kwars. """
        value_format = '%Y-%m-%dT%H:%M:%S.%f'

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                