#!/usr/bin/python3
"""The BaseModel

Contains a class BaseModel that defines all common attributes/
methods for other classes
"""

from datetime import datetime
import uuid


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
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                # set the attribute with the given key and value
                setattr(self, key, value)
        else:
            # generate a unique id
            self.id = str(uuid.uuid4())
            # assign the current datetime
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

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
