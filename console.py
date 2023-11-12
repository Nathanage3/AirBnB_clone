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

    def do_count(self, class_name):
        """Counts the number of instances of a given class."""
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == class_name:
                count += 1
        print(count)

    def do_show_id(self, class_name, obj_id):
        """Show an instance based on its class name and id."""
        key = f"{class_name}.{obj_id}"
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy_id(self, class_name, obj_id):
        """Destroy an instance based on its class name and id."""
        key = f"{class_name}.{obj_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()  # Assuming you have a method to save changes to storage
        else:
            print("** no instance found **")

    def do_update_id_with_dict(self, class_name, obj_id, attr_dict):
        """Update an instance based on its class name and id with a dictionary."""
        key = f"{class_name}.{obj_id}"
        if key in storage.all():
            obj = storage.all()[key]
            for attr_name, attr_value in attr_dict.items():
                if hasattr(obj, attr_name):
                    setattr(obj, attr_name, attr_value)
            obj.save()  # Assuming you have a method to save changes to storage
        else:
            print("** no instance found **")
            
    def default(self, line):
        """Handle default case when command prefix is not recognized."""
        
        if '.' in line:
            parts = line.split('.', 1)  # Split only on the first dot
            class_name, command = parts[0], parts[1]

        if command.startswith("all()"):
            if self._validate_class_name(class_name):
                self.do_all(class_name)
        elif command.startswith("count()"):
            if self._validate_class_name(class_name):
                self.do_count(class_name)
        elif command.startswith("show("):
            obj_id = command[5:-1].strip('"')
            if self._validate_class_name(class_name):
                self.do_show_id(class_name, obj_id)
        elif command.startswith("destroy("):
            obj_id = command[8:-1].strip('"')
            if self._validate_class_name(class_name):
                self.do_destroy_id(class_name, obj_id)
        elif command.startswith("update("):
            try:
                args = command[7:-1]
                if args[0] == "{":
                    attr_dict = json.loads(args)
                    self.do_update_id_with_dict(class_name, attr_dict)
                else:
                    parts = args.split(',', 1)
                    obj_id = parts[0].strip('" ')
                    attr_dict = json.loads(parts[1].strip())
                    self.do_update_id_with_dict(class_name, obj_id, attr_dict)
            except (json.JSONDecodeError, IndexError):
                print("** invalid format **")
        else:
            print("Unknown command: " + line)
    
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()