#!/usr/bin/python3
""" Base class """
import uuid
from datetime import datetime
import models
format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Base class model that defines all
    methods and attributes for the other classes """
    def __init__(self, *args, **kwargs):
        """ Constructor to initialize the attribute with args and kwars """
        if kwargs:

            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(
                    kwargs["created_at"], format)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], format)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

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
        if "created_at" in dictionary:
            dictionary["created_at"] = dictionary["created_at"].strftime(
                format)
        if "updated_at" in dictionary:
            dictionary["updated_at"] = dictionary["updated_at"].strftime(
                format)
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
