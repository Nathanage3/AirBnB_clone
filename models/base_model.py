#!/usr/bin/python3
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
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the BaseModel instance.
        """
        a = self.__class__.__name__
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
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
