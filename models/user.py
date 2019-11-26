#!/usr/bin/python3
from models.base_model import BaseModel
"""
User - create object for User that inheritance from BaseModel
"""


class User(BaseModel):
    """Public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
