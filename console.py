#!/usr/bin/python3
"""
Command Line Interpreter source code for managing the
serialization and deserialization, attributes and
methods of the object classes present in the AirBnB clone.
"""
import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import models.engine.file_storage

classe = {
        "BaseModel": BaseModel(),
        "Amenity": Amenity(),
        "City": City(),
        "Place": Place(),
        "State": State(),
        "User": User(),
        "Review": Review()
}

my_dict = ["BaseModel", "User"]
line = list()


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    # ----- basic HBNB commands -----

    def do_EOF(self, line):
        """Command to exit the program"""
        return True

    def do_quit(self, line):
        """Command to exit the program"""
        return True

    def emptyline(self):
        """Handles when entering an empty line."""
        pass

    def do_create(self, line):
        """ Method for creating a new class instance."""
        # If line exists
        if line:

            # Compare given class name against list of classes
            for name in my_dict:

                # If found correct ClassName
                if line == name:
                    x = eval(name)()  # Create instance
                    storage.new(x)  # Store instance
                    storage.save()  # Save changes onto file
                    print(x.id)  # Print id of created instance
                    break

                # If couldn't find a correct ClassName
                else:
                    print("** class doesn't exist **")

        # If line empty
        else:
            print("** class name missing **")

    def do_show(self, line):
        """ Method that prints the string representation of an instance
        based on the class name and id. """

        # If line exists.
        if line:
            # Slipt arguments.
            args = line.split(" ")
            if len(args) == 0:
                print("** class name missing **")
                return
            # for name in my_dict:
            if args[0] not in classe:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
            # If given an id
            if len(args) > 1:
                # Create ClassName.id string
                key = args[0] + "." + args[1]
                # Run through dictionary
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_all(self, line):
        """ Method for printing all the objects """
        # Reload all instances from the .json file
        storage.reload()
        # Get the dictionary of objects
        dicto = storage.all()
        # Create empty list for printing
        args = line.split(" ")
        # Asks if class name is in classe dict
        if args[0] not in classe:
            print("** class doesn't exist **")
        else:
            # Create empty list for printing
            list_of_str = []
            # If line exists
            if line:
                # If class name is in dicto
                for obj in dicto.keys():
                    if args[0] in obj:
                        # append their str representation
                        list_of_str.append(str(dicto[obj]))
                print(list_of_str)

    def do_destroy(self, line):
        """Method for destroying an object using its id"""
        if line:
            args = line.split(' ')
            # Compare given class name against list of classes
            if len(args) > 1:
                # Create ClassName.id string
                key = args[0] + "." + args[1]
            if not args[0] and len(args) == 1:
                print("** class name missing **")
            elif args[0] not in classe:
                print("** class doesn't exist **")
            elif key not in models.storage.all():
                print("** no instance found **")
            else:
                models.storage.all().pop(key)
                models.storage.save()

    def do_update(self, line):
        """Method for destroying an object using its id"""
        args = line.split(' ')
        # Compare given class name against list of classes
        if len(args) > 1:
            # Create ClassName.id string
            key = args[0] + "." + args[1]
        if not args[0] and len(args) == 1:
            print("** class name missing **")
        elif args[0] not in classe:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif key not in models.storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            setattr(models.storage.all()[key], args[2], args[3])
            models.storage.save()

if __name__ == '__main__':
    # Start running the cmd loop
    HBNBCommand().cmdloop()
