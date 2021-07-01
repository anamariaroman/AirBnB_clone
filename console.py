#!/usr/bin/python3
"""
Command Line Interpreter source code for managing the
serialization and deserialization, attributes and
methods of the object classes present in the AirBnB clone.
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome to the HBNB shell.   Type help or ? to list commands.\n'
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

if __name__ == '__main__':
    # Start running the cmd loop
    HBNBCommand().cmdloop()
