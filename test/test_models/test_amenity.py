#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Defines test cases for the Amenity class."""

    def test_init(self):
        """Test initialization of Amenity instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_inheritance(self):
        """Test if Amenity inherits from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Test Amenity attributes."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_types(self):
        """Test the type of Amenity attributes."""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(amenity.name, str)

    def test_save(self):
        """Test the save method of Amenity."""
        amenity = Amenity()
        updated_at_before = amenity.updated_at
        amenity.save()
        updated_at_after = amenity.updated_at
        self.assertNotEqual(updated_at_before, updated_at_after)

    # Add more tests related to Amenity-specific behavior

if __name__ == "__main__":
    unittest.main()
