#!/usr/bin/python3
"""User modele."""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits the properties of BaseModel."""

    def __int__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        