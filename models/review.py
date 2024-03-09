#!/usr/bin/python3
"""creates a class review that inherits
    from Basemodel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """creates a review class"""
    place_id = ""
    user_id = ""
    text = ""
