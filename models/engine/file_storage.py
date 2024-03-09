#!/usr/bin/python3
"""Module: file_storage.py

Defines a 'file storgae' class
"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage():
    __file_path = "file.json"
    _objects = {}

    def all(self):
        """Returns the dictionary _objects"""
        return FileStorage._objects

    def new(self, obj):
        """sets in _objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage._objects[key] = obj

    def save(self):
        """serializes _objects to the json file"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for
                       k, v in FileStorage._objects.items()}, f)

    def reload(self):
        """deserializes the json file to __objects only if the json
        file exists"""

        current_classes = {'BaseModel': BaseModel, 'User': User,
                   'City': City, 'Review': Review, 'Amenity': Amenity,
                   'Place': Place, 'State': State}

        if not os.path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return
            FileStorage._objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()
            }
