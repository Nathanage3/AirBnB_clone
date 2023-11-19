#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""

import os
import unittest
from models import storage
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Defines test cases for the Amenity class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data.
        """
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

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

    def test_str(self):
        """Test method for str representation
        """
        a1 = Amenity()
        string = f"[{type(a1).__name__}] ({a1.id}) {a1.__dict__}"
        self.assertEqual(a1.__str__(), string)
    
    def test_todict(self):
        """Test method for dict
        """
        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        a_dict = a2.to_dict()
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(a2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(a1, a2)
    # Add more tests related to Amenity-specific behavior

if __name__ == "__main__":
    unittest.main()
