#!/usr/bin/python3
""" Script that contains a class FileStorage """

import json
import models


class FileStorage():
    """ This class that serializes instances to a JSON
        file and deserialize JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Method that returns the dict __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Method that sets in __objects the obj with key
        <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Method that serializes __objects to the JSON file
        (path: __file_path) """
        obj = {}
        for key, the_value in FileStorage.__objects.items():
            obj[key] = the_value.to_dict()
        with open(FileStorage.__file_path ,"W") as file:
            json.dump(obj, file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
        with open(FileStorage.__file_path ,"r") as file:
            json.load(file)
                for key in file
                    self.__objects[key] =
