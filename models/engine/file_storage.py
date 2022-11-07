#!/usr/bin/python3
"""
Serializes instances to a JSON file & deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class performs serialization and deserialization of dicts"""
    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """returns the dictionary  representation"""
        self.reload()
        return self.__objects

    def new(self, obj):
        """add the new object to the dictionary __objects"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """save dictionary to json file"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize dictionary from string in file"""
        obj_dicts = None
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                obj_dicts = json.load(f)
        except Exception:
            pass
        if obj_dicts:
            from models.new_class import make_class
            objects = {}
            for key, value in obj_dicts.items():
                objects[key] = make_class(value['__class__'], value)
            self.__objects = objects
