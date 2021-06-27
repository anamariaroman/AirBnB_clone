#!/usr/bin/python3
""" Base class """
import uuid
from datetime import datetime
import json

class BaseModel:
    """ Base class model that contains the all methods and attributes for the some classes """

    def __init__(self, *args, **kwargs):
        """ Constructor to initialize the attribute with args and kwars. """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        value_format = '%Y-%m-%dT%H:%M:%S.%f'

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                