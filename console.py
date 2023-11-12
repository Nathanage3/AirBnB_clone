#!/usr/bin/python3
"""A module for HBNBCommand"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


valid_classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
               "City": City, "State": State, "Place": Place, "Review": Review} 

class HBNBCommand(cmd.Cmd):
    """User input command for python interpreter"""
    prompt = '(hbnb) '

    valid_classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
               "City": City, "State": State, "Place": Place, "Review": Review}

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
        """Creates a new instance of a class"""
        class_name = args.split()[0] if args else ""
        if class_name in self.valid_classes:
            new_instance = self.valid_classes[class_name]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **" if class_name else "** class name missing **")

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

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating an attribute."""
        arg = args.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return
        cl_name, ins_id, attr_name, attr_value = arg[:4]
        if not self._validate_class_name(cl_name):
            return
        all_objs = storage.all()
        obj_key = "{}.{}".format(cl_name, ins_id)
        if obj_key not in all_objs:
            print("** no instance found **")
            return
        if attr_name in ["id", "created_at", "updated_at"]:
            return
        instance = all_objs[obj_key]
        try:
            attr_value = eval(attr_value)
        except Exception as e:
            pass
        setattr(instance, attr_name, attr_value)
        instance.save()

    def default(self, line):
        """Handle default case when command prefix is not recognized."""
        if '.' in line and line.endswith('.all()'):
            class_name = line.split('.')[0]
            if self._validate_class_name(class_name):
                self.do_all(class_name)
        else:
            print("Unknown command: " + line)    

if __name__ == "__main__":
    HBNBCommand().cmdloop()