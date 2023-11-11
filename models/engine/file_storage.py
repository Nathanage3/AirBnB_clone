#!/usr/bin/python3
''' FileStorage class for serialization and deserialization of instances '''

import os
import json
from models.base_model import BaseModel
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.user import User


class FileStorage():
    """
    FileStorage class that serializes instances to a JSON file and
    deserializes JSON file to instances.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(FileStorage.__file_path, 'w') as f:
            json_objects = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(json_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if the JSON file (__file_path) exists.
        """
        new_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}
        if not os.path.exists(FileStorage.__file__path):
            return
            
        with open(FileStorage.__file_path, 'r') as f:
            objects = None
            
            try:
                objects = json.loads(f)

            except Exception as e:
                pass

            if objects is None:
                return

            FileStorage.__objects = {
                k: new_classes[k.split('.')[0]](**v)
                for k, v in objects.items()
            }
        

