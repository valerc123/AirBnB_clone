#!/usr/bin/python3
from models.base_model import BaseModel
"""
Review - create object for review
"""


class Review(BaseModel):
    """Public class attributes"""
    place_id = ""
    user_id = ""
    text = ""
