#!/usr/bin/python3
"""creates a class City that inherits
    from Basemodel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """creates a city class"""
    state_id = ""
    name = ""
