#!/usr/bin/python3
"""creates class from the available list"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


def make_class(cls, kwargs=None):
    """returns instance of a class"""
    if kwargs is None:
        return eval(cls)()
    else:
        return eval(cls)(**kwargs)
