#!/usr/bin/python3
""" Script that contains a class FileStorage """

import json
from models.base_model import BaseModel
classe = {
        "BaseModel": BaseModel,
}


class FileStorage():
    """ This class that serializes instances to a JSON
        file and deserialize JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Method that returns the dict __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ This Method that sets in __objects the obj with key
        <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ This Method that serializes __objects to the JSON file
        (path: __file_path) """
        obj = {}
        for key, value in FileStorage.__objects.items():
            obj[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                f = json.load(file)
                for key in f:
                    self.__objects[key] = classe[f[key]
                                                  ["__class__"]](**f[key])
        except BaseException:
            pass
