#!/usr/bin/python3
"""
Unit tests for the State class.
"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):
    """Defines test cases for the State class."""

    def test_init(self):
        """Test initialization of State instance."""
        state = State()
        self.assertIsInstance(state, State)

    def test_inheritance(self):
        """Test if State inherits from BaseModel."""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """Test State attributes."""
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_types(self):
        """Test the type of State attributes."""
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(state.name, str)

    def test_save(self):
        """Test the save method of State."""
        state = State()
        updated_at_before = state.updated_at
        state.save()
        updated_at_after = state.updated_at
        self.assertNotEqual(updated_at_before, updated_at_after)

    # Add more tests related to State-specific behavior

if __name__ == "__main__":
    unittest.main()
