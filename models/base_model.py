#!/usr/bin/python3
""" Base class """
import uuid
from datetime import datetime
import json


class BaseModel:
    """ Base class model that contains the all
    methods and attributes for the some classes """

    def __init__(self):
        """ Constructor to initialize the attribute with args and kwars. """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        value_format = '%Y-%m-%dT%H:%M:%S.%f'

    def __str__(self):
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

"""def save(self):
 actualiza el atributo de instancia updated_at con datetime actual

def to_dict(self):
 retorna un diccionario que contiene todas las key/values de la
 instancia __dict__
 created_at y updated_at debesn convertirse a objeto de cadena en formato ISO:
format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)"""
