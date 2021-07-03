#!/usr/bin/python3
"""
Command Line Interpreter source code for managing the
serialization and deserialization, attributes and
methods of the object classes present in the AirBnB clone.
"""
import cmd
from models.base_model import BaseModel
from models import storage
classe = {
        "BaseModel": BaseModel,
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
            #for name in my_dict:
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

if __name__ == '__main__':
    # Start running the cmd loop
    HBNBCommand().cmdloop()
