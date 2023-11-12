#!/usr/bin/python3
"""
Unit tests for the Review class.
"""

import os
import unittest
from models.review import Review
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Defines test cases for the Review class."""

    def test_init(self):
        """Test initialization of Review instance."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_inheritance(self):
        """Test if Review inherits from BaseModel."""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Test Review attributes."""
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_types(self):
        """Test the type of Review attributes."""
        review = Review()
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_save(self):
        """Test the save method of Review."""
        review = Review()
        updated_at_before = review.updated_at
        review.save()
        updated_at_after = review.updated_at
        self.assertNotEqual(updated_at_before, updated_at_after)

    # Add more tests related to Review-specific behavior

if __name__ == "__main__":
    unittest.main()
