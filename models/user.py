#!/usr/bin/python3
"""User modele."""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits the properties of BaseModel."""

    def __int__(self):
        email = ""
        password = ""
        first_name = ""
        last_name = ""
        