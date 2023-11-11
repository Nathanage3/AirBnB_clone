#!/usr/bin/python3
"""Review Module."""


from models.base_model import BaseModel



class Review(BaseModel):
    """Represents a Review for HBNB project."""
    place_id = ""  
    user_id = ""
    text = ""
