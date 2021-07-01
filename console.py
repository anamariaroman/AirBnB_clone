#!/usr/bin/python3
"""
Command Line Interpreter source code for managing the
serialization and deserialization, attributes and
methods of the object classes present in the AirBnB clone.
"""
import cmd
from models.base_model import BaseModel
from models import storage


my_dict = ["BaseModel", "User"]
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

if __name__ == '__main__':
    # Start running the cmd loop
    HBNBCommand().cmdloop()
