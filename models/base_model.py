#!/usr/bin/python
''' BaseModel for all classes'''

from uuid import uuid4
from datetime import datetime

class BaseModel():
    '''Defines all commom attributes and methods for all classes'''

    def __init__(self, *args, **kwargs):
        ''' Initialization of the base model '''
        if kwargs:
            # Assign values from kwargs if present, excluding the key __class__
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        # Convert these string dates to datetime objects
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            # Assign id and dates if not created from a dictionary
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        '''String representation of the BaseModel'''
        a = self.__class__.__name__
        return "[{}] ({}) {}".format(a, self.id, self.__dict__)

    def save(self):
        '''Update the updated_at with the current time'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values'''
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
