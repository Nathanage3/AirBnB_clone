#!/usr/bin/python3
"""A module for HBNBCommand"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """User input command for python interpreter"""
    prompt = '(hbnb) '
    valid_classes = ["BaseModel"]  # Centralized valid classes

    def _validate_class_name(self, class_name):
        """Validate if the class name exists."""
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return False
        return True

    def do_EOF(self, args):
        """EOF command to exit the program. Usage <ctrl + d>"""
        print('\nExiting')
        return True

    def do_quit(self, args):
        """Quit command to exit the program. Usage <quit>"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_help(self, args):
        """Lists available commands in HBNBCommand"""
        super().do_help(args)

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        if not args:
            print('** class name missing **')
            return
        if not self._validate_class_name(args):
            return
        new_model = BaseModel()
        new_model.save()
        print(new_model.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on class name and id."""
        arg = args.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        if len(arg) == 1:
            print('** instance id missing **')
            return
        if not self._validate_class_name(arg[0]):
            return
        all_objs = storage.all()
        obj_key = "{}.{}".format(arg[0], arg[1])
        if obj_key in all_objs:
            print(all_objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if not self._validate_class_name(arg[0]):
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        obj_key = "{}.{}".format(arg[0], arg[1])
        if obj_key in all_objs:
            del all_objs[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        arg = args.split()
        all_objs = storage.all()
        if len(arg) > 0 and not self._validate_class_name(arg[0]):
            return
        instances = [str(value) for key, value in all_objs.items() if len(arg) == 0 or key.startswith(arg[0])]
        print(instances)

    def default(self, args):
        """Yell at the user for wrong input commands"""
        print("Unknown command " + args)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
