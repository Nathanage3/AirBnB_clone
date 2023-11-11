#!/usr/bin/python3
"""City module."""


from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City for HBNB project."""
    state_id = ""  # State.id
    name = ""
