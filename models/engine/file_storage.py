#!/usr/bin/python3
"""Serialization and Deserialization.

Contains a class thaf serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """A class that handles file storage of instances"""

    # path to the JSON file
    __file_path = "file.json"
    # the dictionary that stores all objects by <class name>.id
    __objects = {}
    # the class name of the object
    __class_names = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State
    }

    def all(self):
        """returns the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        # get the class name and id of the object
        class_name = obj.__class__.__name__
        # set the value as the object
        self.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        dictionary = {}

        # iterate over the __objects dictionary
        for key, value in self.__objects.items():
            # convert each value (object) to a dictionary representation
            dictionary[key] = value.to_dict()

        # open the file in write mode
        with open(self.__file_path, 'w') as file:
            # dump the dictionary to the file in JSON format
            json.dump(dictionary, file, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn't
        exist, no exception should be raised"""

        try:
            with open(self.__file_path, 'r') as file:
                # load the dictionary from the file in JSON format
                dictionary = json.load(file)

                # iterate over the dictionary items
                for key, value in dictionary.items():
                    # get the class name from the dictionary values
                    class_name = value['__class__']

                    # get the class from the __class_names dict
                    cls = self.__class_names[class_name]

                    # create an instance of the class from the dictionary
                    # representation
                    obj = cls(**value)

                    # set the instance in the __objects dictionary
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
