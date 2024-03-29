#!/usr/bin/python3
"""The command line Interpreter Modue"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """A command interpreter for HBNB"""

    prompt = '(hbnb) '
    classes = {
        'BaseModel':BaseModel,
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
    }

    # define the method to exit the program
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    # define the method to handle EOF (end-of-file) inpu
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    # define the method to handle empty line input
    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel. Usage: create BaseModel"""

        # check if the class name is given
        if arg == "":
            print("** class name missing **")

        # check if the class name is valid
        elif arg not in self.classes:
            print("** class doesn't exist **")

        else:
            # Create a new instance of the class
            obj = self.classes[arg]()
            # save the instance to the JSON file
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Show the string rep of an instance based on the class name and id"""
        # split the args by space
        args = arg.split()

        # check if the name is give:
        if len(args) == 0:
            print("** the class is missing **")

        # check if the class name is valid
        elif args[0] not in self.classes:
            print("** class doesn't exist **")

        # check if the id is given
        elif len(args) == 1:
            print("** instance id missing **")

        else:
            # get the class name and id from the arguments
            class_name, obj_id = (args[0], args[1])

            # create the key with the format <class name>.<id>
            obj_key = class_name + "." + obj_id

            # get the dictionary of all instances from the storage
            objects = storage.all()
            # check if the key exists in the dictionary
            if obj_key in objects:
                # print the string representation of the object
                obj = objects[obj_key]
                print(obj)

            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance by the class name and id
        Usage: destroy <class name> <id>"""
        # split the args by space
        args = arg.split()

        # check if the name is give:
        if len(args) == 0:
            print("** the class is missing **")

        # check if the class name is valid
        elif args[0] not in self.classes:
            print("** class doesn't exist **")

        # check if the id is given
        elif len(args) == 1:
            print("** instance id missing **")

        else:
            # get the class name and id from the arguments
            class_name, obj_id = (args[0], args[1])

            # create the key with the format <class name>.<id>
            obj_key = class_name + "." + obj_id

            # get the dictionary of all instances from the storage
            objects = storage.all()
            # check if the key exists in the dictionary
            if obj_key in objects:
                # delete the object from the dictionary
                objects.pop(obj_key)
                # save the change to the JSON file
                storage.save()

            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Show all string representation of all instances or instances of\
        a specific class. Usage: all [<class name>]
        """

        # split the arguments by space
        args = arg.split()

        if len(args) == 0:
            # get the dictionary of all instances from the storage
            objects = storage.all()
            # create an empty list to store the string representations
            list_str = []
            # iterate over the dictionary items
            for key, value in objects.items():
                # append to the list
                list_str.append(str(value))

            print(list_str)

        # check if the class name is valid
        elif args[0] not in self.classes:
            print("** class doesn't exist **")

        else:
            # get the class name
            class_name = args[0]
            # get the dictionary of all instances from the storage
            objects = storage.all()
            # create an empty list to store the string representations
            list_str = []
            # iterate over the dictionary items
            for key, value in objects.items():
                if key.startswith(class_name):
                    # append to the list
                    list_str.append(str(value))

            # print the list
            print(list_str)

    def do_update(self, arg):
        """Update an instance based on the class name and id by adding
        or updating attribute"""
        # split the arguments by space
        args = arg.split()
        # check if the class name is given
        if len(args) == 0:
            # print an error message
            print("** class name missing **")
        # check if the class name is valid
        elif args[0] not in self.classes:
            # print an error message
            print("** class doesn't exist **")
        # check if the id is given
        elif len(args) == 1:
            # print an error message
            print("** instance id missing **")
        # check if the attribute name is given
        elif len(args) == 2:
            # print an error message
            print("** attribute name missing **")
        # check if the value for the attribute name is given
        elif len(args) == 3:
            # print an error message
            print("** value missing **")
        else:
            # get the class name, id, attr name and value from the args
            class_name = args[0]
            obj_id = args[1]
            attr_name = args[2]
            attr_value = args[3]
            # create the key with the format <class name>.<id>
            key = class_name + "." + obj_id
            # get the dictionary of all instances from the storage
            objects = storage.all()
            # check if the key exists in the dictionary
            if key in objects:
                # get the object from the dictionary
                obj = objects[key]
                # check if the attribute name is valid
                if attr_name in ["id", "created_at", "updated_at"]:
                    # print an error message
                    print("** attribute cannot be updated **")
                else:
                    # try to cast the value to the attribute type
                    try:
                        attr_type = type(getattr(obj, attr_name))
                        attr_value = attr_type(attr_value)
                    except AttributeError:
                        # if the attribute does not exist, assume its a string
                        attr_value = str(attr_value)
                    # set the attribute with the given value
                    setattr(obj, attr_name, attr_value)
                    # save the change to the JSON file
                    storage.save()
            else:
                # print an error message
                print("** no instance found **")

    def default(self, arg):
        """Handle commands of the form <class name>.all()"""
        # split arguments by dot
        args = arg.split('.')
        # check if the arguments have two elements
        if len(args) == 2:
            # get the class name and the method name from the arguments
            class_name = args[0]
            method_name = args[1]
            # check if class name is valid
            if class_name in self.classes:
                # check if the method name is all
                if method_name == 'all()':
                    self.do_all(class_name)
                elif method_name == 'count()':
                    self.do_count(class_name)
                else:
                    print("*** Unknown syntax: {}".format(arg))
            else:
                print("*** Unknown syntax: {}".format(arg))
        else:
            print("*** Unknown syntax: {}".format(arg))

    def do_count(self, arg):
        """Count the number of instances of a class"""
        # get the class name from the argument
        class_name = arg
        # get the dictionary of all instances from the storage
        objects = storage.all()

        counter = 0

        for key in objects.keys():
            # check if the key starts with the class name
            if key.startswith(class_name):
                counter += 1
        print(counter)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
