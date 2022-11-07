#!/usr/bin/python3
"""
class State that inherits from BaseModel
module state.py describes the class state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class state defines data for a state"""
    name = ""
