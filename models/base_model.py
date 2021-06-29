#!/usr/bin/python3
""" Base class """
import uuid
from datetime import datetime
import models

class BaseModel:
    """ Base class model that defines all
    methods and attributes for the other classes """

    def __init__(self, *args, **kwargs):
        """ Constructor to initialize the attribute with args and kwars """
        value_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            type_number = type(kwargs["created_at"])
            type_check = type(kwargs["updated_at"])
            if "created_at" in kwargs and type_number is str:
                self.created_at = datetime.strptime(
                    kwargs["created_at"], value_format)

            if "updated_at" in kwargs and type_check is str:
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], value_format)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Representation string of the information """
        return "[{}] ({}) {}"\
            .format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing
        all key/values of __dict__ of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
