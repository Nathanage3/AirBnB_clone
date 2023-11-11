#!/usr/bin/python3
"""
Unit tests for User class
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_is_instance(self):
        """Test if the object is an instance of User and BaseModel"""
        my_user = User()
        self.assertIsInstance(my_user, User)
        self.assertIsInstance(my_user, BaseModel)

    def test_attributes(self):
        """Test if the object has the correct attributes"""
        my_user = User()
        self.assertTrue(hasattr(my_user, "id"))
        self.assertTrue(hasattr(my_user, "created_at"))
        self.assertTrue(hasattr(my_user, "updated_at"))
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertTrue(hasattr(my_user, "last_name"))

    def test_attribute_types(self):
        """Test if attributes are of correct type"""
        my_user = User()
        self.assertIsInstance(my_user.id, str)
        self.assertIsInstance(my_user.created_at, datetime)
        self.assertIsInstance(my_user.updated_at, datetime)
        self.assertIsInstance(my_user.email, str)
        self.assertIsInstance(my_user.password, str)
        self.assertIsInstance(my_user.first_name, str)
        self.assertIsInstance(my_user.last_name, str)

    def test_save_method(self):
        """Test if save method updates 'updated_at' attribute"""
        my_user = User()
        old_updated_at = my_user.updated_at
        my_user.save()
        new_updated_at = my_user.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test if to_dict method returns a dictionary"""
        my_user = User()
        user_dict = my_user.to_dict()
        self.assertIsInstance(user_dict, dict)

if __name__ == '__main__':
    unittest.main()
