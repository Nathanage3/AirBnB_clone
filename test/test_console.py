
#!/usr/bin/python3
"""
Unit tests for the HBNBCommand class in console.py.
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestHBNBCommand(unittest.TestCase):
    """Defines test cases for the HBNBCommand class."""

    def setUp(self):
        """Set up the test case."""
        self.console = HBNBCommand()

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_emptyline(self):
        """Test an empty line input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd(""))

    def test_help(self):
        """Test the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("help"))

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertIn('BaseModel', f.getvalue())

    def test_show(self):
        """Test the show command."""
        obj = BaseModel()
        obj.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(obj.id))
            self.assertIn(obj.id, f.getvalue())

    # Additional tests for other commands (destroy, all, update, etc.)

    def tearDown(self):
        """Clean up after tests."""
        try:
            del (obj)
        except Exception:
            pass
        storage.save()


if __name__ == "__main__":
    unittest.main()
     