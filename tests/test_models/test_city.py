#!/usr/bin/python3
"""
Unit tests for the City class.
"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from datetime import datetime

class TestCity(unittest.TestCase):
    """Defines test cases for the City class."""

    def test_init(self):
        """Test initialization of City instance."""
        city = City()
        self.assertIsInstance(city, City)

    def test_inheritance(self):
        """Test if City inherits from BaseModel."""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """Test City attributes."""
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_types(self):
        """Test the type of City attributes."""
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_save(self):
        """Test the save method of City."""
        city = City()
        updated_at_before = city.updated_at
        city.save()
        updated_at_after = city.updated_at
        self.assertNotEqual(updated_at_before, updated_at_after)

    # Add more tests related to City-specific behavior

if __name__ == "__main__":
    unittest.main()
