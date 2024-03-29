#!/usr/bin/python3
"""The BaseModel

Contains a class BaseModel that defines all common attributes/
methods for other classes
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """A base class for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize the instance attributes"""
        # if kwargs is not empty
        if kwargs:
            # iterate over the dictionary items
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at' 'updated_at'):
                    value = datetime.fromisoformat(value)

                # set the attribute with the given key and value
                setattr(self, key, value)
        else:
            # generate a unique id
            self.id = str(uuid4())
            # assign the current datetime
            self.created_at = datetime.now()

            # call the new method on storage with self as argument
            self.updated_at = self.created_at

            # call the new method on storage with self as argument
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        # copy the instance dictionary
        dictionary = self.__dict__.copy()
        # add the class name
        dictionary['__class__'] = self.__class__.__name__
        # convert the datetime objects to ISO format strings
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary
