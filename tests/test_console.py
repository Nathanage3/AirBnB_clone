#!/usr/bin/python3
"""
Unit tests for the HBNBCommand class in console.py.
"""

from io import StringIO
import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review



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

    def test_do_create_valid_class(self):
        """Test 'create' command with a valid class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_do_create_invalid_class(self):
        """Test 'create' command with an invalid class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create FakeClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_do_create_no_class(self):
        """Test 'create' command with no class specified."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "User.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "City.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Review.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())


    def create_base_model_instance(self):
        """Helper method to create and return a BaseModel instance."""
        instance = BaseModel()
        instance.save()
        return instance

    def test_do_show_valid(self):
        """Test 'show' command with a valid class and ID."""
        instance = self.create_base_model_instance()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {instance.id}")
            self.assertIn(instance.id, f.getvalue().strip())

    def test_do_show_invalid_class(self):
        """Test 'show' command with an invalid class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show FakeClass 1234")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_do_show_no_class(self):
        """Test 'show' command with no class specified."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_do_show_no_id(self):
        """Test 'show' command with no ID specified."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())
    
    def test_do_all_with_valid_class(self):
        """Test 'all' command with a valid class name."""
        instance = self.create_base_model_instance()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertIn(instance.id, f.getvalue().strip())

    def test_do_all_with_no_class(self):
        """Test 'all' command with no class name."""
        self.create_base_model_instance()  # Create at least one instance
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)  # Expecting some output

    def test_do_all_with_invalid_class(self):
        """Test 'all' command with an invalid class name."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all FakeClass")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_do_destroy_valid(self):
        """Test 'destroy' command with valid class name and id."""
        instance = self.create_base_model_instance()
        instance_key = f"BaseModel.{instance.id}"
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {instance.id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "")
            self.assertNotIn(instance_key, storage.all())

    def test_do_destroy_invalid_class(self):
        """Test 'destroy' command with an invalid class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy FakeClass 1234")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_do_destroy_no_class(self):
        """Test 'destroy' command with no class specified."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_do_destroy_no_id(self):
        """Test 'destroy' command with class name but no id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())
    def test_do_update_valid(self):
        """Test 'update' command with valid parameters."""
        instance = self.create_base_model_instance()
        new_value = "New Value"
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {instance.id} test_attr '{new_value}'")
            output = f.getvalue().strip()
            self.assertEqual(output, "")
            self.assertEqual(getattr(storage.all()[f"BaseModel.{instance.id}"], "test_attr", ""), new_value)

    def test_do_update_invalid_class(self):
        """Test 'update' command with an invalid class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update FakeClass 1234 attr_name 'attr_value'")
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_do_update_no_class(self):
        """Test 'update' command with no class specified."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **", f.getvalue().strip())

    def test_do_update_no_id(self):
        """Test 'update' command with class name but no id."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual("** instance id missing **", f.getvalue().strip())

    def test_do_update_no_attribute_name(self):
        """Test 'update' command with missing attribute name."""
        instance = self.create_base_model_instance()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {instance.id}")
            self.assertEqual("** attribute name missing **", f.getvalue().strip())

    def test_do_update_no_attribute_value(self):
        """Test 'update' command with missing attribute value."""
        instance = self.create_base_model_instance()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {instance.id} test_attr")
            self.assertEqual("** value missing **", f.getvalue().strip())

    # Additional tests for other commands (destroy, all, update, etc.)
 
    def tearDown(self):
        storage.delete_all() 


if __name__ == "__main__":
    unittest.main()