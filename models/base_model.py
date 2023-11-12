#!/usr/bin/python3
'''
"""
This module defines the BaseModel class, the base class for all models in the hbnb clone.
"""

from uuid import uuid4
from datetime import datetime
import models

               
class BaseModel:
    """A base class for all hbnb models."""

    def __init__(self, *args, **kwargs):
        """
        Instantiates a new BaseModel instance with given attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the BaseModel instance.
        """
        a = type(self).__name__
        return "[{}] ({}) {}".format(a, self.id, self.__dict__)

    def save(self):
        """
        Updates the instance's updated_at timestamp and signals the storage to save it.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.
        """
        dictionary = {**self.__dict__}
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        return dictionary
'''
import models
import uuid
from datetime import datetime


class BaseModel():
    """A base class for all hbnb models.
    """

    def __init__(self, *args, **kwargs):
        """
        instatiates an object with it's
        attributes.
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation
        of the instances.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        """
        dict = {**self.__dict__}
        dict['__class__'] = type(self).__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()

        return dict