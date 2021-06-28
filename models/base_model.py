#!/usr/bin/python3
""" Base class """
import uuid
from datetime import datetime
import json


class BaseModel:
    """ Base class model that defines all
    methods and attributes for the other classes """

    def __init__(self):
        """ Constructor to initialize the attribute with args and kwars """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        value_format = '%Y-%m-%dT%H:%M:%S.%f'

    def __str__(self):
        """ Representation string of the information """
        return "[{}] ({}) {}"\
            .format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing
        all key/values of __dict__ of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
