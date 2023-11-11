#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_init_no_args(self):
        """
        Test BaseModel initialization with no arguments.
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """
        Test BaseModel initialization with keyword arguments.
        """
        kwargs = {
            "id": "1234",
            "created_at": "2021-02-04T21:03:54.052298",
            "updated_at": "2021-02-04T21:03:54.052302"
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, "1234")
        self.assertEqual(model.created_at.isoformat(), "2021-02-04T21:03:54.052298")
        self.assertEqual(model.updated_at.isoformat(), "2021-02-04T21:03:54.052302")

    def test_str(self):
        """
        Test the string representation of the BaseModel instance.
        """
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(model.__str__(), expected_str)

    def test_save(self):
        """
        Test the save method of the BaseModel instance.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of the BaseModel instance.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

if __name__ == '__main__':
    unittest.main()
