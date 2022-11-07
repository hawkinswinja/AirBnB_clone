#!/usr/bin/python3
"""
class Amenity that inherits from BaseModel
module amenity. defines a single class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines all amenities availed by the Airbnb"""
    name = ""
